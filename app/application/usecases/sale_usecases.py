from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    SaleModel,
    SaleItemModel,
    ProductModel,
    InventoryMovementModel
)
from app.services.ticket_service import (
    TicketService
)

session = SessionLocal()


def create_sale(items, customer_id=None):

    total = 0

    sale = SaleModel(
        total=0,
        customer_id=customer_id
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

    items_db = (
        session.query(SaleItemModel)
        .filter(
            SaleItemModel.sale_id == sale.id
        )
        .all()
    )

    TicketService.generate_ticket(
        sale,
        items_db,
        f"ticket_sale_{sale.id}.pdf"
    )

    return sale


def get_products():

    return (
        session.query(ProductModel)
        .all()
    )
