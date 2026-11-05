from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from database import get_db
import models

router = APIRouter(prefix="/api/bids", tags=["Bids"])


# Pydantic Şemaları
class CreateBidRequest(BaseModel):
    product_id: int
    user_id: int
    amount: float
    message: Optional[str] = None


class BidResponse(BaseModel):
    id: int
    product_id: int
    user_id: int
    amount: float
    message: Optional[str]
    created_at: str

    class Config:
        from_attributes = True


# 1. Yeni Teklif Ekleme Endpoint'i
@router.post("", status_code=status.HTTP_201_CREATED)
def create_bid(bid_data: CreateBidRequest, db: Session = Depends(get_db)):
    # Ürün kontrolü
    product = db.query(models.Product).filter(models.Product.id == bid_data.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı!")

    if not product.is_active:
        raise HTTPException(status_code=400, detail="Bu ilan artık tekliflere kapalı!")

    # Yeni teklif oluşturma
    new_bid = models.Bid(
        user_id=bid_data.user_id,
        product_id=bid_data.product_id,
        amount=bid_data.amount,
        message=bid_data.message
    )
    
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    
    return {
        "message": "Teklif başarıyla oluşturuldu!",
        "bid_id": new_bid.id,
        "amount": new_bid.amount
    }


# 2. Belirli Ürüne Ait Teklifleri Getirme Endpoint'i
@router.get("/{product_id}")
def get_bids_by_product(product_id: int, db: Session = Depends(get_db)):
    # Sadece ilgili ürüne ait teklifleri çeker
    bids = (
        db.query(models.Bid)
        .filter(models.Bid.product_id == product_id)
        .order_by(models.Bid.created_at.desc())
        .all()
    )
    return bids
