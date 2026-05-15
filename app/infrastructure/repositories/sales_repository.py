from app.infrastructure.db.connection import SessionLocal

from app.infrastructure.db.models import (
    SaleModel,
    SaleItemModel,
    ProductModel,
    InventoryMovementModel
)


class SalesRepository:

    def __init__(self):

        self.session = SessionLocal()

    def create_sale(
        self,
        user_id,
        items
    ):

        total = 0

        sale_items = []

        for item in items:

            product = self.session.get(
                ProductModel,
                item["product_id"]
            )

            subtotal = (
                product.price
                * item["quantity"]
            )

            total += subtotal

            sale_items.append({
                "product": product,
                "quantity": item["quantity"],
                "price": product.price,
                "subtotal": subtotal
            })

        sale = SaleModel(
            user_id=user_id,
            total=total
        )

        self.session.add(sale)

        self.session.flush()

        for item in sale_items:

            sale_item = SaleItemModel(
                sale_id=sale.id,
                product_id=item["product"].id,
                quantity=item["quantity"],
                price=item["price"],
                subtotal=item["subtotal"]
            )

            self.session.add(sale_item)

            # descontar stock
            item["product"].stock -= (
                item["quantity"]
            )

            # movimiento inventario
            movement = InventoryMovementModel(
                product_id=item["product"].id,
                type="OUT",
                quantity=item["quantity"]
            )

            self.session.add(movement)

        self.session.commit()

        return sale

    def get_all_sales(self):

        return (
            self.session.query(
                SaleModel
            )
            .order_by(
                SaleModel.id.desc()
            )
            .all()
        )

    def get_sale_items(
        self,
        sale_id
    ):

        return (
            self.session.query(
                SaleItemModel
            )
            .filter(
                SaleItemModel.sale_id == sale_id
            )
            .all()
        )
