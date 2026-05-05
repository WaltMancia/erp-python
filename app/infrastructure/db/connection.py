from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ⚠️ Ajusta estas credenciales
DB_USER = "root"
DB_PASSWORD = "123$"
DB_HOST = "localhost"
DB_NAME = "erp_db"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()