from app.infrastructure.repositories.inventory_repository import (
    InventoryRepository
)

from app.core.exceptions import (
    ValidationError
)

repo = InventoryRepository()


def add_stock(
    product_id,
    quantity
):

    try:

        quantity = int(quantity)

    except ValueError:

        raise ValidationError(
            "Cantidad inválida"
        )

    if quantity <= 0:

        raise ValidationError(
            "La cantidad debe ser mayor a 0"
        )

    repo.add_stock(
        product_id,
        quantity
    )


def remove_stock(
    product_id,
    quantity
):

    try:

        quantity = int(quantity)

    except ValueError:

        raise ValidationError(
            "Cantidad inválida"
        )

    if quantity <= 0:

        raise ValidationError(
            "La cantidad debe ser mayor a 0"
        )

    repo.remove_stock(
        product_id,
        quantity
    )


def list_movements():

    return repo.get_movements()
