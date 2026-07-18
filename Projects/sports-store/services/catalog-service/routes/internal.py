from fastapi import APIRouter, Depends, HTTPException

from database import products_collection
from models import StockItem
from security import get_current_user

router = APIRouter(
    prefix="/internal",
    tags=["internal"],
    dependencies=[Depends(get_current_user)],
)


def find_variant(doc: dict | None, sku: str) -> dict | None:
    if doc is None:
        return None
    return next((v for v in doc["variants"] if v["sku"] == sku), None)


@router.get("/variants/{sku}")
async def get_variant(sku: str):
    doc = await products_collection.find_one(
        {"variants.sku": sku, "is_active": True}
    )
    variant = find_variant(doc, sku)
    if variant is None:
        raise HTTPException(status_code=404, detail="SKU not found")
    return {
        "product_id": str(doc["_id"]),
        "name": doc["name"],
        "image_url": doc.get("image_url", ""),
        "sku": variant["sku"],
        "color": variant["color"],
        "size": variant["size"],
        "price": variant["price"],
        "stock_quantity": variant["stock_quantity"],
    }


@router.post("/stock/check")
async def check_stock(items: list[StockItem]):
    results = []
    for item in items:
        doc = await products_collection.find_one(
            {"variants.sku": item.sku, "is_active": True}
        )
        variant = find_variant(doc, item.sku)
        available = variant["stock_quantity"] if variant else 0
        results.append(
            {
                "sku": item.sku,
                "available": available,
                "in_stock": available >= item.quantity,
            }
        )
    return results


@router.post("/stock/decrement")
async def decrement_stock(items: list[StockItem]):
    # No rollback of earlier items on partial failure — an accepted MVP gap
    # (see README: reservations/sagas are the Phase 2 exercise).
    failed = []
    for item in items:
        result = await products_collection.update_one(
            {
                "variants": {
                    "$elemMatch": {
                        "sku": item.sku,
                        "stock_quantity": {"$gte": item.quantity},
                    }
                }
            },
            {"$inc": {"variants.$.stock_quantity": -item.quantity}},
        )
        if result.modified_count == 0:
            failed.append(item.sku)
    if failed:
        raise HTTPException(
            status_code=409,
            detail={"message": "Insufficient stock", "skus": failed},
        )
    return {"message": "Stock decremented"}
