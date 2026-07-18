from datetime import datetime, timezone

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, Depends, HTTPException, Query
from pymongo.errors import DuplicateKeyError

from database import products_collection
from models import ProductCreate, ProductUpdate
from security import require_admin

router = APIRouter(prefix="/products", tags=["products"])


def serialize(doc: dict) -> dict:
    doc["_id"] = str(doc["_id"])
    return doc


def parse_object_id(product_id: str) -> ObjectId:
    try:
        return ObjectId(product_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid product id")


@router.get("")
async def list_products(
    category: str | None = None,
    gender: str | None = None,
    tag: str | None = None,
    q: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    skip: int = Query(default=0, ge=0),
):
    query: dict = {"is_active": True}
    if category:
        query["category"] = category
    if gender:
        query["gender"] = gender
    if tag:
        query["tags"] = tag
    if q:
        query["$text"] = {"$search": q}

    products = []
    async for doc in products_collection.find(query).skip(skip).limit(limit):
        products.append(serialize(doc))
    return products


@router.get("/{slug}")
async def get_product(slug: str):
    doc = await products_collection.find_one({"slug": slug, "is_active": True})
    if doc is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return serialize(doc)


@router.post("", status_code=201, dependencies=[Depends(require_admin)])
async def create_product(payload: ProductCreate):
    doc = payload.model_dump()
    doc["is_active"] = True
    doc["created_at"] = datetime.now(timezone.utc)
    try:
        result = await products_collection.insert_one(doc)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Slug or SKU already exists")
    return {"id": str(result.inserted_id)}


@router.put("/{product_id}", dependencies=[Depends(require_admin)])
async def update_product(product_id: str, payload: ProductUpdate):
    oid = parse_object_id(product_id)
    updates = {k: v for k, v in payload.model_dump().items() if v is not None}
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    result = await products_collection.update_one({"_id": oid}, {"$set": updates})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated"}


@router.delete("/{product_id}", dependencies=[Depends(require_admin)])
async def delete_product(product_id: str):
    oid = parse_object_id(product_id)
    result = await products_collection.update_one(
        {"_id": oid}, {"$set": {"is_active": False}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deactivated"}
