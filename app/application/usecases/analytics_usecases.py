from sqlalchemy import func

from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    SaleModel,
    ProductModel
)

session = SessionLocal()


def sales_by_day():

    results = (
        session.query(
            func.date(
                SaleModel.created_at
            ),
            func.sum(
                SaleModel.total
            )
        )
        .group_by(
            func.date(
                SaleModel.created_at
            )
        )
        .all()
    )

    return results


def low_stock_products():

    return (
        session.query(ProductModel)
        .filter(ProductModel.stock <= 5)
        .all()
    )
