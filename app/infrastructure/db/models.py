from sqlalchemy import Column, Integer, String, Float
from .connection import Base
from datetime import datetime
from sqlalchemy import DateTime
from app.infrastructure.db.connection import Base
from sqlalchemy import (
    ForeignKey,
    DateTime
)

from datetime import datetime


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)


class CustomerModel(Base):

    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    nit = Column(
        String(30),
        nullable=False,
        unique=True
    )

    phone = Column(
        String(20)
    )

    email = Column(
        String(100)
    )

    address = Column(
        String(255)
    )


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


class SaleModel(Base):

    __tablename__ = "sales"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    total = Column(
        Float,
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class SaleItemModel(Base):

    __tablename__ = "sale_items"

    id = Column(
        Integer,
        primary_key=True
    )

    sale_id = Column(
        Integer,
        ForeignKey("sales.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    subtotal = Column(
        Float,
        nullable=False
    )
