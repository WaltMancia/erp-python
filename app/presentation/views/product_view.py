from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QLabel, QTableWidget,
    QTableWidgetItem, QMessageBox, QHeaderView
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

        # Inputs
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre del producto")

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Precio")

        # Botón
        self.add_button = QPushButton("Agregar producto")
        self.add_button.setObjectName("primary")
        self.add_button.clicked.connect(self.add_product)

        # Tabla profesional
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Nombre", "Precio"])

        # Ajustes PRO
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Layout
        layout.addWidget(QLabel("Nombre"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Precio"))
        layout.addWidget(self.price_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.table)

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
        products = list_products()

        self.table.setRowCount(len(products))

        for row, p in enumerate(products):
            self.table.setItem(row, 0, QTableWidgetItem(p.name))
            self.table.setItem(row, 1, QTableWidgetItem(f"Q{p.price:.2f}"))