from pydentic import BaseModel, Field
from datatime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description="Product name")
    slug: str = Field(..., min_length=5, max_length=200, description="URL friendly product name")
    description: str = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Product price(must be greater than zero)")
    image_url: Optional[str] = Field(None, description="Product image url")
    category_id: int = Field(..., description="Category id")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description="Product id")
    name = str
    description = str
    price = float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category = CategoryResponse = Field(..., description="Product category")

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    id: int = Field(..., description="Product id")
    name = str
    description = str
    price = float
    category_id: int
    image_url: Optional[str]