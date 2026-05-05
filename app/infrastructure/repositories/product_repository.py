from app.infrastructure.db.connection import SessionLocal
from app.infrastructure.db.models import ProductModel

class ProductRepository:

    def add(self, product):
        session = SessionLocal()
        try:
            db_product = ProductModel(
                name=product.name,
                price=product.price
            )
            session.add(db_product)
            session.commit()
        finally:
            session.close()

    def get_all(self):
        session = SessionLocal()
        try:
            return session.query(ProductModel).all()
        finally:
            session.close()