from app.infrastructure.repositories.product_repository import (
    ProductRepository
)

from app.core.exceptions import (
    ValidationError
)

repo = ProductRepository()


def create_product(name, price):

    if not name.strip():

        raise ValidationError(
            "El nombre es obligatorio"
        )

    try:
        price = float(price)

    except ValueError:

        raise ValidationError(
            "El precio debe ser numérico"
        )

    if price < 0:

        raise ValidationError(
            "El precio no puede ser negativo"
        )

    repo.create(name, price)


def list_products():

    return repo.get_all()


def update_product(
    product_id,
    name,
    price
):

    if not name.strip():

        raise ValidationError(
            "El nombre es obligatorio"
        )

    try:
        price = float(price)

    except ValueError:

        raise ValidationError(
            "El precio debe ser numérico"
        )

    if price < 0:

        raise ValidationError(
            "El precio no puede ser negativo"
        )

    repo.update(
        product_id,
        name,
        price
    )


def delete_product(product_id):

    repo.delete(product_id)
