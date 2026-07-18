from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials

import orchestrator
from database import orders_collection
from models import CheckoutRequest
from security import bearer_scheme, get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])


def serialize(doc: dict) -> dict:
    doc = dict(doc)
    doc.pop("_id", None)
    return jsonable_encoder(doc)


@router.post("/checkout")
async def checkout(
    payload: CheckoutRequest,
    user: dict = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    order = await orchestrator.checkout(
        user, credentials.credentials, payload.shipping_address, payload.card_number
    )
    body = serialize(order)
    if order["status"] != "paid":
        return JSONResponse(status_code=402, content=body)
    return body


@router.get("")
async def list_orders(user: dict = Depends(get_current_user)):
    orders = []
    cursor = orders_collection.find({"user_id": user["sub"]}).sort("created_at", -1)
    async for doc in cursor:
        orders.append(serialize(doc))
    return orders


@router.get("/{order_number}")
async def get_order(order_number: str, user: dict = Depends(get_current_user)):
    doc = await orders_collection.find_one({"order_number": order_number})
    if doc is None or (doc["user_id"] != user["sub"] and user.get("role") != "admin"):
        raise HTTPException(status_code=404, detail="Order not found")
    return serialize(doc)
