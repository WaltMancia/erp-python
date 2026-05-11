from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from PySide6.QtCore import Qt


class StockDialog(QDialog):

    def __init__(
        self,
        product,
        action
    ):
        super().__init__()

        self.product = product
        self.action = action

        self.setWindowTitle(
            f"{action} stock"
        )

        self.setMinimumWidth(350)

        layout = QVBoxLayout()

        title = QLabel(
            f"{action} inventario"
        )

        title.setObjectName("dialogTitle")

        layout.addWidget(title)

        product_label = QLabel(
            f"Producto: {product.name}"
        )

        layout.addWidget(product_label)

        stock_label = QLabel(
            f"Stock actual: {product.stock}"
        )

        layout.addWidget(stock_label)

        self.quantity_input = QLineEdit()

        self.quantity_input.setPlaceholderText(
            "Cantidad"
        )

        layout.addWidget(
            self.quantity_input
        )

        save_btn = QPushButton(
            "Guardar"
        )

        save_btn.setObjectName("primary")

        save_btn.clicked.connect(
            self.validate
        )

        layout.addWidget(save_btn)

        self.setLayout(layout)

    def validate(self):

        quantity = self.quantity_input.text()

        if not quantity.isdigit():

            QMessageBox.warning(
                self,
                "Error",
                "Cantidad inválida"
            )

            return

        self.accept()

    def get_quantity(self):

        return int(
            self.quantity_input.text()
        )