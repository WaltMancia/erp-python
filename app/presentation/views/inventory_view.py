from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QHeaderView
)

from PySide6.QtCore import Qt

from app.application.usecases.product_usecases import (
    list_products
)

from app.application.usecases.inventory_usecases import (
    add_stock,
    remove_stock
)

from app.presentation.dialogs.stock_dialog import (
    StockDialog
)


class InventoryView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel(
            "Inventario"
        )

        title.setObjectName("pageTitle")

        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Producto",
            "Precio",
            "Stock",
            "Estado",
            "Acciones"
        ])

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        self.table.verticalHeader().setDefaultSectionSize(
            60
        )

        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_data()

    def load_data(self):

        products = list_products()

        self.table.setRowCount(
            len(products)
        )

        for row, p in enumerate(products):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(p.name)
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(f"Q{p.price:.2f}")
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(str(p.stock))
            )

            # ===== STATUS =====

            status = QLabel()

            if p.stock <= 5:

                status.setText(
                    "⚠ Bajo"
                )

                status.setObjectName(
                    "stockLow"
                )

            else:

                status.setText(
                    "✔ Disponible"
                )

                status.setObjectName(
                    "stockOk"
                )

            status.setAlignment(
                Qt.AlignCenter
            )

            self.table.setCellWidget(
                row,
                3,
                status
            )

            # ===== ACTIONS =====

            actions = QHBoxLayout()

            add_btn = QPushButton(
                "+ Stock"
            )

            add_btn.setObjectName(
                "successBtn"
            )

            remove_btn = QPushButton(
                "- Stock"
            )

            remove_btn.setObjectName(
                "dangerBtn"
            )

            add_btn.clicked.connect(
                lambda _, p=p:
                self.add_stock_ui(p)
            )

            remove_btn.clicked.connect(
                lambda _, p=p:
                self.remove_stock_ui(p)
            )

            actions.addWidget(add_btn)
            actions.addWidget(remove_btn)

            container = QWidget()

            container.setLayout(actions)

            self.table.setCellWidget(
                row,
                4,
                container
            )

    def add_stock_ui(self, product):

        dialog = StockDialog(
            product,
            "Agregar"
        )

        if dialog.exec():

            try:

                add_stock(
                    product.id,
                    dialog.get_quantity()
                )

                self.load_data()

            except Exception as e:

                QMessageBox.warning(
                    self,
                    "Error",
                    str(e)
                )

    def remove_stock_ui(self, product):

        dialog = StockDialog(
            product,
            "Retirar"
        )

        if dialog.exec():

            try:

                remove_stock(
                    product.id,
                    dialog.get_quantity()
                )

                self.load_data()

            except Exception as e:

                QMessageBox.warning(
                    self,
                    "Error",
                    str(e)
                )
