from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    SaleModel,
    SaleItemModel,
    ProductModel,
    InventoryMovementModel
)


session = SessionLocal()


def create_sale(items):

    total = 0

    sale = SaleModel(
        total=0
    )

    session.add(sale)

    session.commit()

    for item in items:

        product = session.get(
            ProductModel,
            item["product_id"]
        )

        if not product:
            raise Exception(
                "Producto no encontrado"
            )

        if product.stock < item["quantity"]:
            raise Exception(
                f"Stock insuficiente para {product.name}"
            )

        subtotal = (
            product.price *
            item["quantity"]
        )

        total += subtotal

        sale_item = SaleItemModel(
            sale_id=sale.id,
            product_id=product.id,
            quantity=item["quantity"],
            price=product.price,
            subtotal=subtotal
        )

        session.add(sale_item)

        # Descontar stock
        product.stock -= item["quantity"]

        # Movimiento inventario
        movement = InventoryMovementModel(
            product_id=product.id,
            type="SALIDA",
            quantity=item["quantity"]
        )

        session.add(movement)

    sale.total = total

    session.commit()

    return sale


def get_products():

    return (
        session.query(ProductModel)
        .all()
    )
