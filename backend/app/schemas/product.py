from pydantic import BaseModel, Field
from datetime import datetime
from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=255, description="Product name")
    description: str = Field(
        ..., min_length=3, max_length=255, description="Product description"
    )
    price: float = Field(..., gt=0, description="Product price(greater than 0)")
    category_id: int = Field(..., description=" category id")

    image_url: str = Field(..., description="Product image url")


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int = Field(..., description="Product id")
    name: str
    price: float
    category_id: int
    image_url: str
    created_at: datetime = Field(..., description="Product created at")
    category: CategoryResponse = Field(..., description="Product category details")

    class Config:
        form_attributes = True


class ProductListResponse(BaseModel):
    products: list[ProductResponse] = Field(..., description="Products list")
    total: int = Field(..., description="Total products")
