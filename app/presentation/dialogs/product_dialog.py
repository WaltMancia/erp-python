from PySide6.QtWidgets import (
    QLabel,
    QSpinBox,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QDoubleSpinBox
)

from app.presentation.components.base_dialog import (
    BaseDialog
)

from app.presentation.components.validated_input import (
    ValidatedLineEdit
)


class ProductDialog(BaseDialog):

    def __init__(
        self,
        product=None
    ):
        super().__init__(
            "Producto"
        )

        self.product = product

        # ===== NAME =====

        self.name_input = ValidatedLineEdit(
            "Nombre del producto"
        )

        # ===== PRICE =====

        self.price_input = QDoubleSpinBox()

        self.price_input.setMaximum(
            999999
        )

        self.price_input.setDecimals(2)

        self.price_input.setPrefix(
            "Q "
        )

        # ===== STOCK =====

        self.stock_input = QSpinBox()

        self.stock_input.setMaximum(
            999999
        )

        # ===== LOAD DATA =====

        if product:

            self.name_input.setText(
                product.name
            )

            self.price_input.setValue(
                float(product.price)
            )

            self.stock_input.setValue(
                product.stock
            )

        # ===== BUTTONS =====

        buttons = QWidget()

        buttons_layout = QHBoxLayout()

        self.cancel_btn = QPushButton(
            "Cancelar"
        )

        self.save_btn = QPushButton(
            "Guardar"
        )

        self.save_btn.setObjectName(
            "primary"
        )

        self.cancel_btn.clicked.connect(
            self.reject
        )

        self.save_btn.clicked.connect(
            self.submit
        )

        buttons_layout.addWidget(
            self.cancel_btn
        )

        buttons_layout.addWidget(
            self.save_btn
        )

        buttons.setLayout(
            buttons_layout
        )

        # ===== FORM =====

        self.layout.addWidget(
            QLabel("Nombre")
        )

        self.layout.addWidget(
            self.name_input
        )

        self.layout.addWidget(
            QLabel("Precio")
        )

        self.layout.addWidget(
            self.price_input
        )

        self.layout.addWidget(
            QLabel("Stock")
        )

        self.layout.addWidget(
            self.stock_input
        )

        self.layout.addStretch()

        self.layout.addWidget(
            buttons
        )

    def validate(self):

        valid = True

        # ===== CLEAR ERRORS =====

        self.name_input.clear_error()

        # ===== NAME =====

        if not self.name_input.text().strip():

            self.name_input.set_error(
                "El nombre es obligatorio"
            )

            valid = False

        # ===== PRICE =====

        if self.price_input.value() <= 0:

            valid = False

        # ===== STOCK =====

        if self.stock_input.value() < 0:

            valid = False

        return valid

    def submit(self):

        if self.validate():

            self.accept()

    def get_data(self):

        return {
            "name": self.name_input.text(),
            "price": self.price_input.value(),
            "stock": self.stock_input.value()
        }
