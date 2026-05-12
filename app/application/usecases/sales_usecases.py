from app.infrastructure.repositories.sales_repository import (
    SalesRepository
)

from app.core.exceptions import (
    ValidationError
)

repo = SalesRepository()


def create_sale(
    user,
    items
):

    if not items:

        raise ValidationError(
            "La venta está vacía"
        )

    return repo.create_sale(
        user.id,
        items
    )
