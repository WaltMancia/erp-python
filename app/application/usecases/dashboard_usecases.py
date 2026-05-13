from sqlalchemy import func

from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    ProductModel,
    SaleModel,
    InventoryMovementModel
)


session = SessionLocal()


def get_dashboard_metrics():

    total_products = (
        session.query(ProductModel)
        .count()
    )

    low_stock = (
        session.query(ProductModel)
        .filter(ProductModel.stock <= 5)
        .count()
    )

    total_sales = (
        session.query(SaleModel)
        .count()
    )

    revenue = (
        session.query(
            func.sum(SaleModel.total)
        )
        .scalar()
    )

    if revenue is None:
        revenue = 0

    recent_movements = (
        session.query(
            InventoryMovementModel
        )
        .order_by(
            InventoryMovementModel.id.desc()
        )
        .limit(5)
        .all()
    )

    return {
        "total_products": total_products,
        "low_stock": low_stock,
        "total_sales": total_sales,
        "revenue": revenue,
        "recent_movements": recent_movements
    }
