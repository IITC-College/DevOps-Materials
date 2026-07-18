from pydantic import BaseModel, Field


class ChargeRequest(BaseModel):
    idempotency_key: str = Field(min_length=1)
    order_number: str
    amount: float = Field(gt=0)
    currency: str = "USD"
    card_number: str = Field(min_length=12, max_length=19)


class ChargeResponse(BaseModel):
    payment_id: str
    idempotency_key: str
    order_number: str
    amount: float
    currency: str
    card_last4: str
    status: str
