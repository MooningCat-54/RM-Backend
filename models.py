from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    banner_url = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    is_corporate = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    products = relationship("Product", back_populates="owner", cascade="all, delete-orphan")
    bids = relationship("Bid", back_populates="user", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, index=True, nullable=False)
    start_price = Column(Float, nullable=False)
    stock_count = Column(Integer, default=1)
    photo_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    owner = relationship("Profile", back_populates="products")
    bids = relationship("Bid", back_populates="product", cascade="all, delete-orphan")


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="bids")
    user = relationship("Profile", back_populates="bids")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    sender = relationship("Profile", foreign_keys=[sender_id])
    receiver = relationship("Profile", foreign_keys=[receiver_id])