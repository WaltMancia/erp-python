from app.infrastructure.db.connection import engine

# IMPORTANTE:
# importar modelos antes de create_all

from app.infrastructure.db.models import (
    Base,
    ProductModel,
    UserModel,
    InventoryMovementModel
)

# Crear tablas
Base.metadata.create_all(bind=engine)

print("✅ Base de datos inicializada correctamente")
