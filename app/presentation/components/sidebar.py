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

        self.buttons = {}

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

        # ===== LOGO =====

        logo = QLabel("Python ERP")

        logo.setObjectName(
            "sidebarLogo"
        )

        logo.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(logo)

        layout.addSpacing(20)

        # ===== MODULES =====

        self.add_nav_button(
            layout,
            "dashboard",
            "Dashboard",
            "products.view"
        )

        self.add_nav_button(
            layout,
            "products",
            "Productos",
            "products.view"
        )

        self.add_nav_button(
            layout,
            "inventory",
            "Inventario",
            "inventory.view"
        )

        self.add_nav_button(
            layout,
            "sales",
            "Ventas",
            "sales.view"
        )

        self.add_nav_button(
            layout,
            "reports",
            "Reportes",
            "reports.view"
        )

        layout.addStretch()

        # ===== USER =====

        user_label = QLabel(
            f"{user.username}\n({user.role})"
        )

        user_label.setObjectName(
            "sidebarUser"
        )

        user_label.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(user_label)

        self.setLayout(layout)

    def add_nav_button(
        self,
        layout,
        route,
        text,
        permission
    ):

        if not has_permission(
            self.user,
            permission
        ):
            return

        button = QPushButton(text)

        button.setObjectName(
            "sidebarButton"
        )

        button.setCursor(
            Qt.PointingHandCursor
        )

        button.clicked.connect(
            lambda: self.navigate(route)
        )

        self.buttons[route] = button

        layout.addWidget(button)

    def navigate(self, route):

        self.set_active(route)

        self.on_navigate(route)

    def set_active(self, active_route):

        for route, button in self.buttons.items():

            if route == active_route:

                button.setProperty(
                    "active",
                    True
                )

            else:

                button.setProperty(
                    "active",
                    False
                )

            button.style().unpolish(button)
            button.style().polish(button)
