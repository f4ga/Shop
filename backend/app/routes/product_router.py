from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_services import ProductService
from ..schemas.product import ProductResponse, ProductListResponse

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.get_all_product()


@router.get(
    "/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK
)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.get_product_by_id(product_id)


@router.get(
    "/category/{category_id}",
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK,
)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.get_product_by_category(category_id)


@router.get(
    "/search", response_model=ProductListResponse, status_code=status.HTTP_200_OK
)
def search_products(query: str, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.search_product(query)
