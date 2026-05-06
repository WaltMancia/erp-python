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

    def delete(self, product_id):
        session = SessionLocal()
        try:
            product = session.query(ProductModel).get(product_id)
            if product:
                session.delete(product)
                session.commit()
        finally:
            session.close()

    def update(self, product_id, name, price):
        session = SessionLocal()
        try:
            product = session.query(ProductModel).get(product_id)
            if product:
                product.name = name
                product.price = price
                session.commit()
        finally:
            session.close()