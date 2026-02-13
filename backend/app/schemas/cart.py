from pydantic import BaseModel, Field

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., description="Quantity")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, 
                          description="new quantity")


class CartItem(BaseModel):
    product_id: int = Field(..., description="Product ID")
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    image_url: str = Field(..., description="Product image URL")
    subtotal: float = Field(..., description="total price for this item (price * quantity)")
    quantity: int = Field(..., gt=0, 
                          description="Quantity in cart")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of cart items")
    total: float = Field(..., description="Total price of all items in cart")
    items_count: int = Field(..., description="Total quantity of all items in cart")