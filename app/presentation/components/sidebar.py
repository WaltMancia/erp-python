from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon


class Sidebar(QWidget):
    def __init__(self, switch_view_callback):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(10, 20, 10, 10)

        self.product_btn = QPushButton("  Productos")
        self.product_btn.setObjectName("menuButton")
        self.product_btn.setCheckable(True)
        self.product_btn.setChecked(True)
        self.product_btn.setIcon(QIcon("app/presentation/assets/box.svg"))
        self.product_btn.clicked.connect(lambda: self.select("products", switch_view_callback))

        layout.addWidget(self.product_btn)
        layout.addStretch()

        self.setLayout(layout)

    def select(self, view, callback):
        self.product_btn.setChecked(False)

        if view == "products":
            self.product_btn.setChecked(True)

        callback(view)