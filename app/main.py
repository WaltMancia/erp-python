import sys
from PySide6.QtWidgets import QApplication
from app.presentation.views.product_view import ProductView
from app.infrastructure.db.connection import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    init_db()

    app = QApplication(sys.argv)

    window = ProductView()
    window.resize(400, 400)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()