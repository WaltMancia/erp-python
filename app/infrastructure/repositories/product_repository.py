from sqlalchemy.exc import SQLAlchemyError

from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    ProductModel
)

from app.core.logger import logger

from app.core.exceptions import (
    DatabaseError
)


class ProductRepository:

    def create(self, name, price, stock):

        session = SessionLocal()

        try:

            product = ProductModel(
                name=name,
                price=price,
                stock=stock
            )

            session.add(product)

            session.commit()

            logger.info(
                f"Producto creado: {name}"
            )

        except SQLAlchemyError:

            session.rollback()

            logger.exception(
                "Error creando producto"
            )

            raise DatabaseError(
                "Error al crear producto"
            )

        finally:
            session.close()

    def get_all(self):

        session = SessionLocal()

        try:

            return session.query(
                ProductModel
            ).all()

        except SQLAlchemyError:

            logger.exception(
                "Error obteniendo productos"
            )

            raise DatabaseError(
                "Error consultando productos"
            )

        finally:
            session.close()

    def update(
        self,
        product_id,
        name,
        price,
        stock
    ):

        session = SessionLocal()

        try:

            product = (
                session.query(ProductModel)
                .filter_by(id=product_id)
                .first()
            )

            if product:

                product.name = name
                product.price = price
                product.stock = stock
                session.commit()

                logger.info(
                    f"Producto actualizado: {name}"
                )

        except SQLAlchemyError:

            session.rollback()

            logger.exception(
                "Error actualizando producto"
            )

            raise DatabaseError(
                "Error actualizando producto"
            )

        finally:
            session.close()

    def delete(self, product_id):

        session = SessionLocal()

        try:

            product = (
                session.query(ProductModel)
                .filter_by(id=product_id)
                .first()
            )

            if product:

                session.delete(product)

                session.commit()

                logger.info(
                    f"Producto eliminado: {product.name}"
                )

        except SQLAlchemyError:

            session.rollback()

            logger.exception(
                "Error eliminando producto"
            )

            raise DatabaseError(
                "Error eliminando producto"
            )

        finally:
            session.close()
