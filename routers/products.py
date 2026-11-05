from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from database import get_db
import models

router = APIRouter(prefix="/api/products", tags=["Products"])

class ProductCreate(BaseModel):
    user_id: int
    title: str
    content: str
    category: str
    start_price: float
    stock_count: Optional[int] = 1
    photo_url: Optional[str] = None

@router.post("", status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    user = db.query(models.Profile).filter(models.Profile.id == product_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı!")

    new_product = models.Product(
        user_id=product_data.user_id,
        title=product_data.title,
        content=product_data.content,
        category=product_data.category,
        start_price=product_data.start_price,
        stock_count=product_data.stock_count,
        photo_url=product_data.photo_url
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return {
        "message": "Ürün ilanı başarıyla oluşturuldu!",
        "product_id": new_product.id,
        "title": new_product.title
    }

@router.get("")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.is_active == True).all()
    return products