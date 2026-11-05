from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Profile

router = APIRouter(prefix="/profiles", tags=["profiles"])

@router.get("/{user_id}")
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == user_id).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Kullanıcı profili bulunamadı"
        )
    
    return {
        "id": profile.id,
        "username": profile.username,
        "full_name": profile.full_name,
        "email": profile.email,
        "phone": profile.phone,
        "avatar_url": profile.avatar_url,
        "banner_url": profile.banner_url,
        "bio": profile.bio,
        "is_corporate": profile.is_corporate,
        "created_at": profile.created_at
    }

@router.get("")
def get_all_profiles(db: Session = Depends(get_db)):
    profiles = db.query(Profile).all()
    return profiles