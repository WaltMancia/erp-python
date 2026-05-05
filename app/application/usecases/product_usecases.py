from app.domain.product import Product
from app.infrastructure.repositories.product_repository import ProductRepository

repo = ProductRepository()

def create_product(name: str, price: float):
    if not name:
        raise ValueError("El nombre es obligatorio")

    if price <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    product = Product(name, price)
    repo.add(product)

def list_products():
    return repo.get_all()