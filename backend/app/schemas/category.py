from pydantic import BaseModel, Field
from datetime import datetime


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=255, description="Category name")
    slug: str = Field(
        ..., min_length=3, max_length=255, description="URL-friendly category name"
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description=" Unique Category ID")
    created_at: datetime = Field(..., description="Category created at")

    class Config:
        from_attributes = True
