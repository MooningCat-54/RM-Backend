from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
import models

router = APIRouter(prefix="/api", tags=["Auth"])

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(models.Profile).filter(models.Profile.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Bu e-posta adresi zaten kullanımda.")
    
    new_user = models.Profile(
        username=user_data.name,
        full_name=user_data.name,
        email=user_data.email,
        password=user_data.password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message": "Kayıt başarılı!",
        "user_id": new_user.id,
        "name": new_user.full_name,
        "email": new_user.email
    }

@router.post("/login")
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.Profile).filter(
        models.Profile.email == credentials.email,
        models.Profile.password == credentials.password
    ).first()
    
    if not user:
        raise HTTPException(status_code=400, detail="E-posta veya şifre hatalı!")
    
    return {
        "message": "Giriş başarılı!",
        "user_id": user.id,
        "name": user.full_name,
        "email": user.email
    }