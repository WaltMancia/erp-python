from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from app.application.usecases.customer_usecases import (
    list_customers
)


class CustomerView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel(
            "Clientes"
        )

        title.setObjectName(
            "pageTitle"
        )

        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Nombre",
            "NIT",
            "Teléfono",
            "Email",
            "Dirección"
        ])

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(
            self.table
        )

        self.setLayout(layout)

        self.load_data()

    def load_data(self):

        customers = list_customers()

        self.table.setRowCount(
            len(customers)
        )

        for row, customer in enumerate(customers):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(customer.name)
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(customer.nit)
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    customer.phone or ""
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    customer.email or ""
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    customer.address or ""
                )
            )
