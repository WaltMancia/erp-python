from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PySide6.QtGui import (
    QIcon
)

from PySide6.QtCore import QSize


class Sidebar(QWidget):

    def __init__(
        self,
        parent=None
    ):
        super().__init__()

        self.parent = parent

        self.buttons = {}

        self.setObjectName(
            "sidebar"
        )

        self.setFixedWidth(240)

        layout = QVBoxLayout()

        # ===== LOGO =====

        logo = QLabel(
            "ERP PYTHON"
        )

        logo.setObjectName(
            "sidebarLogo"
        )

        layout.addWidget(logo)

        # ===== NAVIGATION =====

        self.add_nav_button(
            layout,
            "dashboard",
            "Dashboard",
            "app/presentation/assets/icons/dashboard.svg"
        )

        self.add_nav_button(
            layout,
            "products",
            "Productos",
            "app/presentation/assets/icons/products.svg"
        )

        self.add_nav_button(
            layout,
            "inventory",
            "Inventario",
            "app/presentation/assets/icons/inventory.svg"
        )

        self.add_nav_button(
            layout,
            "customers",
            "Clientes",
            "app/presentation/assets/icons/customers.svg"
        )

        self.add_nav_button(
            layout,
            "sales",
            "Ventas",
            "app/presentation/assets/icons/sales.svg"
        )

        self.add_nav_button(
            layout,
            "sales_history",
            "Historial",
            "app/presentation/assets/icons/reports.svg"
        )

        layout.addStretch()

        self.setLayout(layout)

    def add_nav_button(
        self,
        layout,
        key,
        text,
        icon_path
    ):

        btn = QPushButton(text)

        btn.setObjectName(
            "sidebarButton"
        )

        btn.setIcon(
            QIcon(icon_path)
        )

        btn.setIconSize(
            QSize(20, 20)
        )

        btn.clicked.connect(
            lambda:
            self.change_page(key)
        )

        layout.addWidget(btn)

        self.buttons[key] = btn

    def change_page(
        self,
        page
    ):

        if self.parent:

            self.parent.switch_page(
                page
            )

        self.set_active(page)

    def set_active(
        self,
        active_key
    ):

        for key, btn in self.buttons.items():

            if key == active_key:

                btn.setObjectName(
                    "sidebarButtonActive"
                )

            else:

                btn.setObjectName(
                    "sidebarButton"
                )

            btn.style().unpolish(btn)
            btn.style().polish(btn)
