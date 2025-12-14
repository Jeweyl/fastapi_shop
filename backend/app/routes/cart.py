from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Dict
from app.database import get_db
from app.services.cart_serveces import CartService, CartResponse
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartResponse
from pydantic import BaseModel  

router = APIRouter(
    prefix="/api/carts",
    tags=['carts']
)

class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int] = {}

class UpdateCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart = Dict[int, int] = {}

class RemoveFromCartRequest(BaseModel):
    cart: Dict[int, int] = {}

@router.post("/add", status_code=status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    update_cart = service.add_to_cart(request.cart, item)
    return {"cart": update_cart}

@router.post("", response_model = CartResponse, status_code=status.HTTP_200_OK)
def get_cart(cart_data: Dict[int, int], db: Session = Depends(get_db)):
    service = CartService(db)
    return service.get_cart_details(cart_data)

@router.put("/update", status_code=status.HTTP_200_OK)
def update_cart_item(request: UpdateCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    update_cart = service.update_cart_item(request.cart, item)
    return {"cart": update_cart}

@router.put("/remove", status_code=status.HTTP_200_OK)
def update_cart_item(product_id: int, request: RemoveFromCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    update_cart = service.update_cart_item(request.cart, product_id)
    return {"cart": update_cart}