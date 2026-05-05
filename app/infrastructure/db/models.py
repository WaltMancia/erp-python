from sqlalchemy import Column, Integer, String, Float
from .connection import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)