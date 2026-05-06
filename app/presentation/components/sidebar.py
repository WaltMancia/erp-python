from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon

class Sidebar(QWidget):
    def __init__(self, switch_view_callback):
        super().__init__()

        self.setFixedWidth(200)

        layout = QVBoxLayout()

        self.product_btn = QPushButton(" Productos")
        self.product_btn.setIcon(QIcon("app/presentation/assets/box.svg"))
        self.product_btn.clicked.connect(lambda: switch_view_callback("products"))

        self.client_btn = QPushButton(" Clientes")
        self.client_btn.setIcon(QIcon("app/presentation/assets/users.svg"))

        self.sales_btn = QPushButton(" Ventas")
        self.sales_btn.setIcon(QIcon("app/presentation/assets/dollar.svg"))

        layout.addWidget(self.product_btn)
        layout.addWidget(self.client_btn)
        layout.addWidget(self.sales_btn)
        layout.addStretch()

        self.setLayout(layout)