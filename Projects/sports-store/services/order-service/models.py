from pydantic import BaseModel, Field


class ShippingAddress(BaseModel):
    full_name: str = Field(min_length=1)
    street: str = Field(min_length=1)
    city: str = Field(min_length=1)
    postal_code: str = Field(min_length=1)
    country: str = Field(min_length=1)


class CheckoutRequest(BaseModel):
    shipping_address: ShippingAddress
    card_number: str = Field(min_length=12, max_length=19)
