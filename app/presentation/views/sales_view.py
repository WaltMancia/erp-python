from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QSpinBox,
    QHBoxLayout,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt

from app.application.usecases.sale_usecases import (
    create_sale,
    get_products
)

from app.application.usecases.customer_usecases import (
    list_customers
)


class SalesView(QWidget):

    def __init__(self):
        super().__init__()

        self.cart = []

        layout = QVBoxLayout()

        # ===== TITLE =====

        title = QLabel(
            "Punto de Venta"
        )

        title.setObjectName(
            "pageTitle"
        )

        layout.addWidget(title)

        # ===== CUSTOMER =====

        customer_row = QHBoxLayout()

        customer_label = QLabel(
            "Cliente:"
        )

        self.customer_combo = QComboBox()

        self.customers = list_customers()

        self.customer_combo.addItem(
            "Consumidor Final",
            None
        )

        for customer in self.customers:

            self.customer_combo.addItem(
                f"{customer.name} | {customer.nit}",
                customer.id
            )

        customer_row.addWidget(
            customer_label
        )

        customer_row.addWidget(
            self.customer_combo
        )

        layout.addLayout(
            customer_row
        )

        # ===== PRODUCT SELECT =====

        row = QHBoxLayout()

        self.product_combo = QComboBox()

        self.products = get_products()

        for product in self.products:

            self.product_combo.addItem(
                f"{product.name} | "
                f"Q{product.price:.2f} | "
                f"Stock: {product.stock}",
                product.id
            )

        self.quantity_input = QSpinBox()

        self.quantity_input.setMinimum(1)

        self.quantity_input.setMaximum(999)

        add_btn = QPushButton(
            "Agregar"
        )

        add_btn.setObjectName(
            "primary"
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

        # ===== CART TABLE =====

        self.cart_table = QTableWidget()

        self.cart_table.setColumnCount(5)

        self.cart_table.setHorizontalHeaderLabels([
            "Producto",
            "Cantidad",
            "Precio",
            "Subtotal",
            "Acciones"
        ])

        header = (
            self.cart_table.horizontalHeader()
        )

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        self.cart_table.verticalHeader().setVisible(
            False
        )

        self.cart_table.setMinimumHeight(
            300
        )

        layout.addWidget(
            self.cart_table
        )

        # ===== TOTAL =====

        self.total_label = QLabel(
            "Total: Q0.00"
        )

        self.total_label.setObjectName(
            "dashboardCardValue"
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

        sale_btn.setMinimumHeight(45)

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

        if quantity > product.stock:

            QMessageBox.warning(
                self,
                "Stock insuficiente",
                "No hay suficiente stock"
            )

            return

        existing = next(
            (
                item for item in self.cart
                if item["product_id"] == product.id
            ),
            None
        )

        if existing:

            existing["quantity"] += quantity

        else:

            self.cart.append({
                "product_id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": quantity
            })

        self.refresh_cart()

    def refresh_cart(self):

        self.cart_table.setRowCount(
            len(self.cart)
        )

        total = 0

        for row, item in enumerate(self.cart):

            subtotal = (
                item["price"] *
                item["quantity"]
            )

            total += subtotal

            self.cart_table.setItem(
                row,
                0,
                QTableWidgetItem(
                    item["name"]
                )
            )

            self.cart_table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(item["quantity"])
                )
            )

            self.cart_table.setItem(
                row,
                2,
                QTableWidgetItem(
                    f"Q{item['price']:.2f}"
                )
            )

            self.cart_table.setItem(
                row,
                3,
                QTableWidgetItem(
                    f"Q{subtotal:.2f}"
                )
            )

            delete_btn = QPushButton(
                "Eliminar"
            )

            delete_btn.setObjectName(
                "deleteBtn"
            )

            delete_btn.clicked.connect(
                lambda _, r=row:
                self.remove_item(r)
            )

            self.cart_table.setCellWidget(
                row,
                4,
                delete_btn
            )

        self.total_label.setText(
            f"Total: Q{total:.2f}"
        )

    def remove_item(self, row):

        self.cart.pop(row)

        self.refresh_cart()

    def complete_sale(self):

        if not self.cart:

            QMessageBox.warning(
                self,
                "Error",
                "El carrito está vacío"
            )

            return

        customer_id = (
            self.customer_combo.currentData()
        )

        try:

            create_sale(
                self.cart,
                customer_id
            )

            QMessageBox.information(
                self,
                "Venta completada",
                "La venta fue registrada correctamente"
            )

            self.cart.clear()

            self.refresh_cart()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )
