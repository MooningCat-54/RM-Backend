from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ReMarket API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/listings")
def get_listings(db: Session = Depends(get_db)):
    return db.query(models.Listing).all()

@app.get("/api/profiles")
def get_profiles(db: Session = Depends(get_db)):
    return db.query(models.Profile).all()