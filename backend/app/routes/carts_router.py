from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Dict
from ..database import get_db
from ..services.cart_services import CartService
from ..schemas.cart import (
    CartResponse,
    CartItemCreate,
    RemoveFromCartRequest,
    CartItemUpdate,
)
from pydantic import BaseModel

router = APIRouter(prefix="/api/cart", tags=["cart"])


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart_data: Dict[int, int] = {}


@router.post("/add", response_model=CartResponse, status_code=status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    cart_service = CartService(db)
    cart_item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = cart_service.add_to_cart(cart_item, request.cart_data)
    return {"cart": updated_cart}


@router.get("/get", response_model=CartResponse, status_code=status.HTTP_200_OK)
def get_cart(cart_data: Dict[int, int], db: Session = Depends(get_db)):
    cart_service = CartService(db)
    return cart_service.get_cart(cart_data)


@router.put("/update", response_model=CartResponse, status_code=status.HTTP_200_OK)
def update_cart(request: CartItemUpdate, db: Session = Depends(get_db)):
    cart_service = CartService(db)
    cart_item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = cart_service.update_cart(cart_item, request.cart_data)
    return {"cart": updated_cart}


@router.delete(
    "/remove/{product_id}", response_model=CartResponse, status_code=status.HTTP_200_OK
)
def remove_from_cart(
    product_id: int, request: RemoveFromCartRequest, db: Session = Depends(get_db)
):
    cart_service = CartService(db)
    updated_cart = cart_service.remove_from_cart(request.cart, product_id)
    return {"cart": updated_cart}
