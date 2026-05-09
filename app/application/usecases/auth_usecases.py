from app.infrastructure.repositories.user_repository import (
    UserRepository
)

from app.infrastructure.security.password_hasher import (
    hash_password,
    verify_password
)

repo = UserRepository()


def register_user(
    username,
    password,
    role="employee"
):

    if not username.strip():
        raise ValueError(
            "El usuario es obligatorio"
        )

    if len(password) < 4:
        raise ValueError(
            "La contraseña debe tener al menos 4 caracteres"
        )

    existing = repo.get_by_username(username)

    if existing:
        raise ValueError(
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
        raise ValueError(
            "Usuario o contraseña incorrectos"
        )

    valid = verify_password(
        password,
        user.password
    )

    if not valid:
        raise ValueError(
            "Usuario o contraseña incorrectos"
        )

    return user
