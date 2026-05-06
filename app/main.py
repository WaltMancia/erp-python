import sys
from PySide6.QtWidgets import QApplication
from app.presentation.views.main_window import MainWindow
from app.infrastructure.db.connection import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)

def load_styles(app):
    with open("app/presentation/styles/style.qss", "r") as f:
        app.setStyleSheet(f.read())

def main():
    init_db()

    app = QApplication(sys.argv)

    load_styles(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()