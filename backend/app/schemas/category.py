from .category import Category
from .product import Product
from pydantic import BaseModel, Field
from datetime import datetime

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=255,
        description = "Category name")
    slug: str = Field(..., min_length=3, max_length=255,
        description = "URL-friendly category slug")
   
    
class CategoryCreate(CategoryBase):
    pass    

class CategoryResponse(CategoryBase):
    id: int = Field(..., description = " Unique Category ID")
    created_at: datetime = Field(..., description = "Category creation date")

    class Config:
        form_attributes = True