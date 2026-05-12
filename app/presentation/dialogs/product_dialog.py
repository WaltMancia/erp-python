from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
    QWidget
)

from PySide6.QtCore import Qt

from app.core.exceptions import (
    ValidationError
)


class ProductDialog(QDialog):

    def __init__(
        self,
        product=None
    ):
        super().__init__()

        self.product = product

        self.setWindowTitle(
            "Producto"
        )

        self.setMinimumWidth(420)

        self.setObjectName(
            "productDialog"
        )

        layout = QVBoxLayout()

        layout.setSpacing(14)

        # ===== TITLE =====

        title = QLabel()

        title.setText(
            "Editar producto"
            if product
            else "Nuevo producto"
        )

        title.setObjectName(
            "dialogTitle"
        )

        layout.addWidget(title)

        # ===== NAME =====

        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Nombre del producto"
        )

        layout.addWidget(
            QLabel("Nombre")
        )

        layout.addWidget(
            self.name_input
        )

        # ===== PRICE =====

        self.price_input = QLineEdit()

        self.price_input.setPlaceholderText(
            "0.00"
        )

        layout.addWidget(
            QLabel("Precio")
        )

        layout.addWidget(
            self.price_input
        )

        # ===== STOCK =====

        self.stock_input = QLineEdit()

        self.stock_input.setPlaceholderText(
            "0"
        )

        layout.addWidget(
            QLabel("Stock inicial")
        )

        layout.addWidget(
            self.stock_input
        )

        # ===== ERROR LABEL =====

        self.error_label = QLabel()

        self.error_label.setObjectName(
            "errorLabel"
        )

        self.error_label.hide()

        layout.addWidget(
            self.error_label
        )

        # ===== BUTTONS =====

        buttons = QHBoxLayout()

        cancel_btn = QPushButton(
            "Cancelar"
        )

        save_btn = QPushButton(
            "Guardar"
        )

        save_btn.setObjectName(
            "primary"
        )

        cancel_btn.clicked.connect(
            self.reject
        )

        save_btn.clicked.connect(
            self.validate
        )

        buttons.addWidget(cancel_btn)
        buttons.addWidget(save_btn)

        layout.addLayout(buttons)

        # ===== LOAD PRODUCT =====

        if product:

            self.name_input.setText(
                product.name
            )

            self.price_input.setText(
                str(product.price)
            )

            self.stock_input.setText(
                str(product.stock)
            )

        self.setLayout(layout)

    def validate(self):

        try:

            name = (
                self.name_input.text()
                .strip()
            )

            if len(name) < 3:

                raise ValidationError(
                    "El nombre debe tener al menos 3 caracteres"
                )

            price = float(
                self.price_input.text()
            )

            if price <= 0:

                raise ValidationError(
                    "El precio debe ser mayor a 0"
                )

            stock = int(
                self.stock_input.text()
            )

            if stock < 0:

                raise ValidationError(
                    "El stock no puede ser negativo"
                )

            self.accept()

        except ValueError:

            self.show_error(
                "Datos inválidos"
            )

        except ValidationError as e:

            self.show_error(str(e))

    def show_error(self, message):

        self.error_label.setText(
            message
        )

        self.error_label.show()

    def get_data(self):

        return {
            "name": self.name_input.text(),
            "price": float(
                self.price_input.text()
            ),
            "stock": int(
                self.stock_input.text()
            )
        }