from pydantic import BaseModel, Field


class AddItemRequest(BaseModel):
    sku: str
    quantity: int = Field(ge=1)


class UpdateItemRequest(BaseModel):
    quantity: int = Field(ge=0)
