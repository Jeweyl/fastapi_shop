from pydentic import BaseModel, Field
from datatime import datetime
from typing import Optional
from .category import CategoryResponse

class CartItemVase(BaseModel):
    product_id: int = Field(..., description="Product id")
    quantity: int = Field(..., gt=0, description="Product quantity(must be greater than zero)")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product id")
    quantity: int = Field(..., gt=0, description="Product quantity(must be greater than zero)") 

class CartItem(BaseModel):
    product_id: int = Field(..., description="Product id")
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Product quantity(must be greater than zero)")
    subtotal: float = Field(..., description="Total price (quantity * price)")
    image_url: Optional[str] = Field(None, description="Product image url")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="Cart items")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total cart items")