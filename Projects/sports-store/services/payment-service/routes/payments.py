from datetime import datetime, timezone
from os import environ

from fastapi import APIRouter, Depends, HTTPException
from pymongo.errors import DuplicateKeyError

from database import payments_collection
from models import ChargeRequest, ChargeResponse
from security import get_current_user

router = APIRouter(
    prefix="/payments",
    tags=["payments"],
    dependencies=[Depends(get_current_user)],
)

FAILURE_SUFFIX = environ.get("PAYMENT_FAILURE_SUFFIX", "0000")


def to_response(doc: dict) -> ChargeResponse:
    return ChargeResponse(
        payment_id=str(doc["_id"]),
        idempotency_key=doc["idempotency_key"],
        order_number=doc["order_number"],
        amount=doc["amount"],
        currency=doc["currency"],
        card_last4=doc["card_last4"],
        status=doc["status"],
    )


@router.post("/charge", response_model=ChargeResponse)
async def charge(payload: ChargeRequest, user: dict = Depends(get_current_user)):
    existing = await payments_collection.find_one(
        {"idempotency_key": payload.idempotency_key}
    )
    if existing:
        return to_response(existing)

    status = "failed" if payload.card_number.endswith(FAILURE_SUFFIX) else "succeeded"
    doc = {
        "idempotency_key": payload.idempotency_key,
        "order_number": payload.order_number,
        "user_id": user["sub"],
        "amount": payload.amount,
        "currency": payload.currency,
        "card_last4": payload.card_number[-4:],
        "status": status,
        "provider": "mock",
        "created_at": datetime.now(timezone.utc),
    }
    try:
        result = await payments_collection.insert_one(doc)
        doc["_id"] = result.inserted_id
    except DuplicateKeyError:
        # Concurrent replay of the same key — return the stored outcome.
        doc = await payments_collection.find_one(
            {"idempotency_key": payload.idempotency_key}
        )
    return to_response(doc)


@router.get("/{idempotency_key}", response_model=ChargeResponse)
async def get_payment(idempotency_key: str):
    doc = await payments_collection.find_one({"idempotency_key": idempotency_key})
    if doc is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return to_response(doc)
