from sqlalchemy import Column, Integer, String, Float
from .connection import Base
from datetime import datetime
from sqlalchemy import DateTime
from app.infrastructure.db.connection import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(50),
        default="employee"
    )


class InventoryMovementModel(Base):

    __tablename__ = "inventory_movements"

    id = Column(
        Integer,
        primary_key=True
    )

    product_id = Column(
        Integer,
        nullable=False
    )

    movement_type = Column(
        String(20),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
