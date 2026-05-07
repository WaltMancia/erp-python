from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from PySide6.QtGui import QDoubleValidator


class ProductDialog(QDialog):
    def __init__(self, product=None):
        super().__init__()

        self.setWindowTitle("Editar producto")
        self.setMinimumWidth(350)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nombre del producto")

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Precio")

        validator = QDoubleValidator(0.0, 999999.99, 2)
        self.price_input.setValidator(validator)

        # Si viene producto (modo edición)
        self.product = product

        if product:
            self.name_input.setText(product.name)
            self.price_input.setText(str(product.price))

        self.save_button = QPushButton("Guardar")
        self.save_button.setObjectName("primary")

        self.save_button.clicked.connect(self.validate)

        layout.addWidget(QLabel("Nombre"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Precio"))
        layout.addWidget(self.price_input)

        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def validate(self):
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()

        if not name:
            QMessageBox.warning(
                self,
                "Validación",
                "El nombre es obligatorio"
            )
            return

        if not price:
            QMessageBox.warning(
                self,
                "Validación",
                "El precio es obligatorio"
            )
            return

        self.accept()

    def get_data(self):
        return {
            "name": self.name_input.text().strip(),
            "price": float(self.price_input.text())
        }
