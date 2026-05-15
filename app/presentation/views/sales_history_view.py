from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
    QDialog,
    QHeaderView
)

from PySide6.QtCore import Qt

from app.application.usecases.sale_usecases import (
    get_sales_history,
    get_sale_detail
)


class SalesHistoryView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel(
            "Historial de Ventas"
        )

        title.setObjectName(
            "pageTitle"
        )

        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Fecha",
            "Cliente",
            "Total",
            "Acciones"
        ])

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.Stretch
        )

        self.table.verticalHeader().setVisible(
            False
        )

        self.table.setMinimumHeight(500)

        layout.addWidget(
            self.table
        )

        self.setLayout(layout)

        self.load_sales()

    def load_sales(self):

        sales = get_sales_history()

        self.table.setRowCount(
            len(sales)
        )

        for row, sale in enumerate(sales):

            customer_name = (
                "Consumidor Final"
            )

            if sale.customer_id:

                customer_name = (
                    f"Cliente #{sale.customer_id}"
                )

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(sale.id)
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(sale.created_at)
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    customer_name
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    f"Q{sale.total:.2f}"
                )
            )

            detail_btn = QPushButton(
                "Ver detalle"
            )

            detail_btn.clicked.connect(
                lambda _, s=sale:
                self.show_detail(s.id)
            )

            self.table.setCellWidget(
                row,
                4,
                detail_btn
            )

    def show_detail(self, sale_id):

        items = get_sale_detail(
            sale_id
        )

        text = ""

        total = 0

        for item in items:

            subtotal = (
                item.price *
                item.quantity
            )

            total += subtotal

            text += (
                f"Producto ID: "
                f"{item.product_id}\n"
                f"Cantidad: "
                f"{item.quantity}\n"
                f"Precio: "
                f"Q{item.price:.2f}\n"
                f"Subtotal: "
                f"Q{subtotal:.2f}\n\n"
            )

        text += f"\nTOTAL: Q{total:.2f}"

        QMessageBox.information(
            self,
            "Detalle Venta",
            text
        )
