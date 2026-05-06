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

def delete_product(product_id: int):
    repo.delete(product_id)

def update_product(product_id: int, name: str, price: float):
    if not name:
        raise ValueError("El nombre es obligatorio")

    if price <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    repo.update(product_id, name, price)