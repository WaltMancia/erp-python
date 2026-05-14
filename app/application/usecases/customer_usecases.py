from app.infrastructure.db.models import (
    CustomerModel
)

from app.infrastructure.repositories.customer_repository import (
    CustomerRepository
)

repo = CustomerRepository()


def list_customers():

    return repo.get_all()


def create_customer(
    name,
    nit,
    phone,
    email,
    address
):

    existing = repo.get_by_nit(nit)

    if existing:

        raise Exception(
            "Ya existe un cliente con ese NIT"
        )

    customer = CustomerModel(
        name=name,
        nit=nit,
        phone=phone,
        email=email,
        address=address
    )

    return repo.create(customer)


def update_customer(
    customer_id,
    name,
    nit,
    phone,
    email,
    address
):

    customer = repo.get_by_id(
        customer_id
    )

    if not customer:

        raise Exception(
            "Cliente no encontrado"
        )

    customer.name = name
    customer.nit = nit
    customer.phone = phone
    customer.email = email
    customer.address = address

    repo.update(customer)


def delete_customer(customer_id):

    customer = repo.get_by_id(
        customer_id
    )

    if not customer:

        raise Exception(
            "Cliente no encontrado"
        )

    repo.delete(customer)
