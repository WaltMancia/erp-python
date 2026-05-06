from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QLabel, QTableWidget,
    QTableWidgetItem, QMessageBox, QHeaderView,
    QHBoxLayout
)

from PySide6.QtCore import Qt


from app.application.usecases.product_usecases import (
    create_product,
    list_products,
    delete_product,
    update_product
)

class ProductView(QWidget):
    def __init__(self):
        super().__init__()

        self.editing_id = None

        layout = QVBoxLayout()
        
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)

        # Inputs
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre del producto")

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Precio")

        self.save_button = QPushButton("Guardar producto")
        self.save_button.setObjectName("primary")
        self.save_button.clicked.connect(self.save_product)

        # Tabla
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Nombre", "Precio", "Acciones"])
        

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        self.table.setColumnWidth(2, 200)
        self.table.setWordWrap(False)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Layout
        layout.addWidget(QLabel("Nombre"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Precio"))
        layout.addWidget(self.price_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.table)
       
        self.setLayout(layout)

        self.load_products()

    def save_product(self):
        try:
            name = self.name_input.text()
            price = float(self.price_input.text())

            if self.editing_id:
                update_product(self.editing_id, name, price)
                self.editing_id = None
                self.save_button.setText("Guardar producto")
            else:
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

            # Botones
            btn_layout = QHBoxLayout()
            btn_layout.setContentsMargins(0, 0, 0, 0)
            btn_layout.setSpacing(5)

            edit_btn = QPushButton("Editar")
            edit_btn.setObjectName("editBtn")

            delete_btn = QPushButton("Eliminar")
            delete_btn.setObjectName("deleteBtn")

            edit_btn.clicked.connect(lambda _, p=p: self.edit_product(p))
            delete_btn.clicked.connect(lambda _, p=p: self.delete_product_ui(p.id))

            btn_layout.addWidget(edit_btn)
            btn_layout.addWidget(delete_btn)

            container = QWidget()
            container.setLayout(btn_layout)

            self.table.setCellWidget(row, 2, container)

    def edit_product(self, product):
        self.editing_id = product.id
        self.name_input.setText(product.name)
        self.price_input.setText(str(product.price))
        self.save_button.setText("Actualizar producto")

    def delete_product_ui(self, product_id):
        confirm = QMessageBox.question(
            self,
            "Confirmar",
            "¿Eliminar producto?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            delete_product(product_id)
            self.load_products()