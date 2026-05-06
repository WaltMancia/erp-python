from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QLabel, QListWidget, QMessageBox
)

from app.application.usecases.product_usecases import (
    create_product,
    list_products
)

class ProductView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ERP - Productos")

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre del producto")

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Precio")

        self.add_button = QPushButton("Agregar producto")
        self.add_button.setObjectName("primary")
        self.add_button.clicked.connect(self.add_product)

        self.list_widget = QListWidget()

        layout.addWidget(QLabel("Nombre"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Precio"))
        layout.addWidget(self.price_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

        self.load_products()

    def add_product(self):
        try:
            name = self.name_input.text()
            price = float(self.price_input.text())

            create_product(name, price)

            self.name_input.clear()
            self.price_input.clear()

            self.load_products()

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def load_products(self):
        self.list_widget.clear()
        products = list_products()

        for p in products:
            self.list_widget.addItem(f"{p.name} - Q{p.price}")