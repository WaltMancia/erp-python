from app.infrastructure.repositories.user_repository import (
    UserRepository
)

from app.infrastructure.security.password_hasher import (
    hash_password,
    verify_password
)

from app.core.exceptions import (
    ValidationError,
    AuthenticationError
)

repo = UserRepository()


def register_user(
    username,
    password,
    role="employee"
):

    allowed_roles = [
        "admin",
        "employee",
        "inventory"
    ]

    if role not in allowed_roles:

        raise ValidationError(
            "Rol inválido"
        )

    if not username.strip():

        raise ValidationError(
            "El usuario es obligatorio"
        )

    if len(password) < 4:

        raise ValidationError(
            "La contraseña debe tener al menos 4 caracteres"
        )

    existing = repo.get_by_username(username)

    if existing:

        raise ValidationError(
            "El usuario ya existe"
        )

    hashed = hash_password(password)

    repo.create(
        username,
        hashed,
        role
    )


def login_user(
    username,
    password
):

    user = repo.get_by_username(username)

    if not user:

        raise AuthenticationError(
            "Usuario o contraseña incorrectos"
        )

    valid = verify_password(
        password,
        user.password
    )

    if not valid:

        raise AuthenticationError(
            "Usuario o contraseña incorrectos"
        )

    return user
