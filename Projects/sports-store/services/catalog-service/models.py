from pydantic import BaseModel, Field


class Variant(BaseModel):
    sku: str
    color: str
    size: str
    price: float = Field(gt=0)
    stock_quantity: int = Field(ge=0)


class ProductCreate(BaseModel):
    name: str
    slug: str
    description: str = ""
    brand: str = "Stryda"
    category: str
    gender: str = "unisex"
    tags: list[str] = []
    image_url: str = ""
    base_price: float = Field(gt=0)
    variants: list[Variant] = Field(min_length=1)


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    category: str | None = None
    gender: str | None = None
    tags: list[str] | None = None
    image_url: str | None = None
    base_price: float | None = Field(default=None, gt=0)
    variants: list[Variant] | None = None
    is_active: bool | None = None


class StockItem(BaseModel):
    sku: str
    quantity: int = Field(ge=1)
