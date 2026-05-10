from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PySide6.QtCore import Qt

from app.core.permissions import (
    has_permission
)


class Sidebar(QWidget):

    def __init__(
        self,
        user,
        on_navigate
    ):
        super().__init__()

        self.user = user

        self.on_navigate = on_navigate

        self.setFixedWidth(240)

        self.setObjectName("sidebar")

        layout = QVBoxLayout()

        layout.setSpacing(10)

        layout.setContentsMargins(
            15,
            20,
            15,
            20
        )

        # Logo
        logo = QLabel("Python ERP")

        logo.setObjectName("sidebarLogo")

        logo.setAlignment(Qt.AlignCenter)

        layout.addWidget(logo)

        layout.addSpacing(20)

        # ===== PRODUCTS =====

        if has_permission(
            user,
            "products.view"
        ):

            btn_products = QPushButton(
                "Productos"
            )

            btn_products.setObjectName(
                "sidebarButton"
            )

            btn_products.clicked.connect(
                lambda: self.on_navigate(
                    "products"
                )
            )

            layout.addWidget(btn_products)

        # ===== INVENTORY =====

        if has_permission(
            user,
            "inventory.view"
        ):

            btn_inventory = QPushButton(
                "Inventario"
            )

            btn_inventory.setObjectName(
                "sidebarButton"
            )

            layout.addWidget(btn_inventory)

        # ===== SALES =====

        if has_permission(
            user,
            "sales.view"
        ):

            btn_sales = QPushButton(
                "Ventas"
            )

            btn_sales.setObjectName(
                "sidebarButton"
            )

            layout.addWidget(btn_sales)

        # ===== REPORTS =====

        if has_permission(
            user,
            "reports.view"
        ):

            btn_reports = QPushButton(
                "Reportes"
            )

            btn_reports.setObjectName(
                "sidebarButton"
            )

            layout.addWidget(btn_reports)

        layout.addStretch()

        # User info
        user_label = QLabel(
            f"{user.username}\n({user.role})"
        )

        user_label.setObjectName(
            "sidebarUser"
        )

        user_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(user_label)

        self.setLayout(layout)
