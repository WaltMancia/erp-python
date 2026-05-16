from sqlalchemy import func

from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    ProductModel,
    SaleModel,
    CustomerModel,
    SaleItemModel
)


session = SessionLocal()


def get_dashboard_stats():

    total_products = (
        session.query(ProductModel)
        .count()
    )

    total_customers = (
        session.query(CustomerModel)
        .count()
    )

    total_sales = (
        session.query(SaleModel)
        .count()
    )

    total_revenue = (
        session.query(
            func.sum(SaleModel.total)
        )
        .scalar()
    ) or 0

    low_stock = (
        session.query(ProductModel)
        .filter(
            ProductModel.stock <= 5
        )
        .count()
    )

    return {
        "products": total_products,
        "customers": total_customers,
        "sales": total_sales,
        "revenue": total_revenue,
        "low_stock": low_stock
    }


def get_top_products():

    results = (
        session.query(
            SaleItemModel.product_id,
            func.sum(
                SaleItemModel.quantity
            ).label("qty")
        )
        .group_by(
            SaleItemModel.product_id
        )
        .order_by(
            func.sum(
                SaleItemModel.quantity
            ).desc()
        )
        .limit(5)
        .all()
    )

    return results
