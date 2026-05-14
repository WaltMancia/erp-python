from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QSpinBox,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QMessageBox
)

from app.application.usecases.sale_usecases import (
    create_sale,
    get_products
)


class SalesView(QWidget):

    def __init__(self):
        super().__init__()

        self.cart = []

        layout = QVBoxLayout()

        title = QLabel(
            "Punto de Venta"
        )

        title.setObjectName(
            "pageTitle"
        )

        layout.addWidget(title)

        # ===== PRODUCT SELECT =====

        row = QHBoxLayout()

        self.product_combo = QComboBox()

        self.products = get_products()

        for product in self.products:

            self.product_combo.addItem(
                f"{product.name} | "
                f"Stock: {product.stock}",
                product.id
            )

        self.quantity_input = QSpinBox()

        self.quantity_input.setMinimum(1)

        add_btn = QPushButton(
            "Agregar"
        )

        add_btn.clicked.connect(
            self.add_to_cart
        )

        row.addWidget(
            self.product_combo
        )

        row.addWidget(
            self.quantity_input
        )

        row.addWidget(
            add_btn
        )

        layout.addLayout(row)

        # ===== CART =====

        self.cart_list = QListWidget()

        layout.addWidget(
            self.cart_list
        )

        # ===== TOTAL =====

        self.total_label = QLabel(
            "Total: Q0.00"
        )

        self.total_label.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(
            self.total_label
        )

        # ===== COMPLETE SALE =====

        sale_btn = QPushButton(
            "Completar Venta"
        )

        sale_btn.setObjectName(
            "primary"
        )

        sale_btn.clicked.connect(
            self.complete_sale
        )

        layout.addWidget(
            sale_btn
        )

        self.setLayout(layout)

    def add_to_cart(self):

        index = (
            self.product_combo.currentIndex()
        )

        product = self.products[index]

        quantity = (
            self.quantity_input.value()
        )

        subtotal = (
            product.price * quantity
        )

        self.cart.append({
            "product_id": product.id,
            "quantity": quantity
        })

        self.cart_list.addItem(
            QListWidgetItem(
                f"{product.name} | "
                f"{quantity} x "
                f"Q{product.price:.2f} "
                f"= Q{subtotal:.2f}"
            )
        )

        self.update_total()

    def update_total(self):

        total = 0

        for item in self.cart:

            product = next(
                p for p in self.products
                if p.id == item["product_id"]
            )

            total += (
                product.price *
                item["quantity"]
            )

        self.total_label.setText(
            f"Total: Q{total:.2f}"
        )

    def complete_sale(self):

        if not self.cart:

            QMessageBox.warning(
                self,
                "Error",
                "El carrito está vacío"
            )

            return

        try:

            create_sale(self.cart)

            QMessageBox.information(
                self,
                "Éxito",
                "Venta completada"
            )

            self.cart.clear()

            self.cart_list.clear()

            self.update_total()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )
