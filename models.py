from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    is_corporate = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profiles.id"))
    title = Column(String, index=True)
    content = Column(String)
    category = Column(String, index=True)
    start_price = Column(Float)
    stock_count = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    start_date = Column(DateTime, default=datetime.utcnow)

class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    user_id = Column(Integer, ForeignKey("profiles.id"))
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("profiles.id"))
    receiver_id = Column(Integer, ForeignKey("profiles.id"))
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)