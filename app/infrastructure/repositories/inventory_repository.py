from sqlalchemy.exc import SQLAlchemyError

from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    ProductModel,
    InventoryMovementModel
)

from app.core.logger import logger

from app.core.exceptions import (
    DatabaseError,
    ValidationError
)


class InventoryRepository:

    def add_stock(
        self,
        product_id,
        quantity
    ):

        session = SessionLocal()

        try:

            product = (
                session.query(ProductModel)
                .filter_by(id=product_id)
                .first()
            )

            if not product:

                raise ValidationError(
                    "Producto no encontrado"
                )

            product.stock += quantity

            movement = InventoryMovementModel(
                product_id=product_id,
                movement_type="IN",
                quantity=quantity
            )

            session.add(movement)

            session.commit()

            logger.info(
                f"Entrada inventario: {product.name} +{quantity}"
            )

        except SQLAlchemyError:

            session.rollback()

            logger.exception(
                "Error agregando stock"
            )

            raise DatabaseError(
                "Error actualizando inventario"
            )

        finally:
            session.close()

    def remove_stock(
        self,
        product_id,
        quantity
    ):

        session = SessionLocal()

        try:

            product = (
                session.query(ProductModel)
                .filter_by(id=product_id)
                .first()
            )

            if not product:

                raise ValidationError(
                    "Producto no encontrado"
                )

            if product.stock < quantity:

                raise ValidationError(
                    "Stock insuficiente"
                )

            product.stock -= quantity

            movement = InventoryMovementModel(
                product_id=product_id,
                movement_type="OUT",
                quantity=quantity
            )

            session.add(movement)

            session.commit()

            logger.info(
                f"Salida inventario: {product.name} -{quantity}"
            )

        except SQLAlchemyError:

            session.rollback()

            logger.exception(
                "Error removiendo stock"
            )

            raise DatabaseError(
                "Error actualizando inventario"
            )

        finally:
            session.close()

    def get_movements(self):

        session = SessionLocal()

        try:

            return (
                session.query(
                    InventoryMovementModel
                )
                .order_by(
                    InventoryMovementModel.id.desc()
                )
                .all()
            )

        finally:
            session.close()
