from app.application.usecases.auth_usecases import (
    register_user
)

from app.core.logger import logger

try:

    register_user(
        username="admin",
        password="Admin123",
        role="admin"
    )

    print("✅ Usuario admin creado")

    logger.info(
        "Admin inicial creado"
    )

except Exception as e:

    print(f"❌ Error: {e}")
