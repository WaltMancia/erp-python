from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    CustomerModel
)


class CustomerRepository:

    def __init__(self):

        self.session = SessionLocal()

    def get_all(self):

        return (
            self.session.query(
                CustomerModel
            ).all()
        )

    def create(
        self,
        customer
    ):

        self.session.add(customer)

        self.session.commit()

        return customer

    def update(self, customer):

        self.session.commit()

    def delete(self, customer):

        self.session.delete(customer)

        self.session.commit()

    def get_by_id(self, customer_id):

        return self.session.get(
            CustomerModel,
            customer_id
        )

    def get_by_nit(self, nit):

        return (
            self.session.query(
                CustomerModel
            )
            .filter(
                CustomerModel.nit == nit
            )
            .first()
        )
