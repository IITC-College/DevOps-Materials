import logging
from datetime import datetime, timezone
from os import environ

from fastapi import HTTPException
from pymongo import ReturnDocument

import clients
from database import counters_collection, orders_collection
from models import ShippingAddress

logger = logging.getLogger("order-service")

SHIPPING_FLAT_RATE = float(environ.get("SHIPPING_FLAT_RATE", "5.00"))
FREE_SHIPPING_THRESHOLD = float(environ.get("FREE_SHIPPING_THRESHOLD", "100"))


async def next_order_number() -> str:
    year = datetime.now(timezone.utc).year
    counter = await counters_collection.find_one_and_update(
        {"_id": f"orders-{year}"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER,
    )
    return f"ORD-{year}-{counter['seq']:06d}"


def build_pricing(items: list[dict]) -> dict:
    subtotal = round(sum(i["quantity"] * i["unit_price"] for i in items), 2)
    shipping = 0.0 if subtotal >= FREE_SHIPPING_THRESHOLD else SHIPPING_FLAT_RATE
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "total": round(subtotal + shipping, 2),
        "currency": "USD",
    }


async def checkout(
    user: dict, token: str, shipping_address: ShippingAddress, card_number: str
) -> dict:
    cart = await clients.get_cart(token)
    items = cart.get("items", [])
    if not items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    stock_items = [{"sku": i["sku"], "quantity": i["quantity"]} for i in items]
    stock = await clients.check_stock(stock_items, token)
    short = [entry["sku"] for entry in stock if not entry["in_stock"]]
    if short:
        raise HTTPException(
            status_code=409,
            detail={"message": "Insufficient stock", "skus": short},
        )

    order_number = await next_order_number()
    order = {
        "order_number": order_number,
        "user_id": user["sub"],
        "status": "pending",
        "items": items,
        "pricing": build_pricing(items),
        "shipping_address": shipping_address.model_dump(),
        "payment": None,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }
    await orders_collection.insert_one(order)

    payment = await clients.charge(
        {
            "idempotency_key": order_number,
            "order_number": order_number,
            "amount": order["pricing"]["total"],
            "currency": order["pricing"]["currency"],
            "card_number": card_number,
        },
        token,
    )

    if payment["status"] == "succeeded":
        decremented = await clients.decrement_stock(stock_items, token)
        if not decremented:
            # Paid but stock update failed — an accepted MVP gap; real systems
            # reserve inventory before charging (see README Phase 2 exercises).
            logger.error("Stock decrement failed after payment for %s", order_number)
        await clients.clear_cart(token)
        new_status = "paid"
    else:
        new_status = "payment_failed"

    order["status"] = new_status
    order["payment"] = {
        "payment_id": payment["payment_id"],
        "idempotency_key": order_number,
    }
    order["updated_at"] = datetime.now(timezone.utc)
    await orders_collection.update_one(
        {"order_number": order_number},
        {"$set": {
            "status": new_status,
            "payment": order["payment"],
            "updated_at": order["updated_at"],
        }},
    )
    return order
