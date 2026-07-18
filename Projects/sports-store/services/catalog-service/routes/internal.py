from fastapi import APIRouter, Depends, HTTPException

from database import products_collection
from models import StockItem
from security import get_current_user

router = APIRouter(
    prefix="/internal/stock",
    tags=["internal"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/check")
async def check_stock(items: list[StockItem]):
    results = []
    for item in items:
        doc = await products_collection.find_one(
            {"variants.sku": item.sku, "is_active": True},
            {"variants.$": 1},
        )
        available = doc["variants"][0]["stock_quantity"] if doc else 0
        results.append(
            {
                "sku": item.sku,
                "available": available,
                "in_stock": available >= item.quantity,
            }
        )
    return results


@router.post("/decrement")
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
