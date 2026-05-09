from app.infrastructure.db.connection import SessionLocal
from app.infrastructure.db.models import UserModel


class UserRepository:

    def create(
        self,
        username,
        password,
        role="employee"
    ):
        session = SessionLocal()

        try:

            user = UserModel(
                username=username,
                password=password,
                role=role
            )

            session.add(user)

            session.commit()

        finally:
            session.close()

    def get_by_username(self, username):

        session = SessionLocal()

        try:

            return session.query(UserModel).filter_by(
                username=username
            ).first()

        finally:
            session.close()
