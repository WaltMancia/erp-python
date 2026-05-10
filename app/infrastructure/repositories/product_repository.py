from sqlalchemy.exc import SQLAlchemyError

from app.infrastructure.db.connection import (
    SessionLocal
)

from app.infrastructure.db.models import (
    UserModel
)

from app.core.logger import logger

from app.core.exceptions import (
    DatabaseError
)


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

            logger.info(
                f"Usuario creado: {username}"
            )

        except SQLAlchemyError as e:

            session.rollback()

            logger.exception(
                "Error creando usuario"
            )

            raise DatabaseError(
                "Error al guardar usuario"
            )

        finally:
            session.close()

    def get_by_username(self, username):

        session = SessionLocal()

        try:

            return (
                session.query(UserModel)
                .filter_by(username=username)
                .first()
            )

        except SQLAlchemyError:

            logger.exception(
                "Error consultando usuario"
            )

            raise DatabaseError(
                "Error consultando usuario"
            )

        finally:
            session.close()
