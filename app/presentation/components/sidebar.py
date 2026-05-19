from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy
)

from PySide6.QtCore import Qt


class Sidebar(QWidget):

    def __init__(
        self,
        user,
        navigate
    ):
        super().__init__()

        self.navigate = navigate

        self.buttons = {}

        self.setObjectName(
            "sidebar"
        )

        self.setFixedWidth(280)

        layout = QVBoxLayout()

        layout.setContentsMargins(
            14,
            20,
            14,
            20
        )

        layout.setSpacing(12)

        # ===== LOGO =====

        logo = QLabel(
            "ERP PYTHON"
        )

        logo.setObjectName(
            "logoText"
        )

        layout.addWidget(
            logo
        )

        layout.addSpacing(20)

        # ===== MENU =====

        menu_items = [

            ("Dashboard", "dashboard"),
            ("Productos", "products"),
            ("Inventario", "inventory"),
            ("Clientes", "customers"),
            ("Ventas", "sales"),
            ("Historial", "sales_history")
        ]

        for text, route in menu_items:

            btn = QPushButton(text)

            btn.setCursor(
                Qt.PointingHandCursor
            )

            btn.setProperty(
                "class",
                "sidebarButton"
            )

            btn.setObjectName(
                "sidebarButton"
            )

            btn.setMinimumHeight(54)

            btn.clicked.connect(
                lambda _, r=route:
                self.navigate(r)
            )

            layout.addWidget(btn)

            self.buttons[route] = btn

        layout.addStretch()

        # ===== USER =====

        user_label = QLabel(
            f"{user.username}\n{user.role.upper()}"
        )

        user_label.setStyleSheet("""
            color: #94a3b8;
            font-size: 13px;
            padding: 10px;
        """)

        layout.addWidget(
            user_label
        )

        self.setLayout(layout)

    def set_active(self, route):

        for r, btn in self.buttons.items():

            if r == route:

                btn.setProperty(
                    "class",
                    "sidebarButtonActive"
                )

                btn.setStyleSheet("""
                    background-color: #2563eb;
                    color: white;
                    border-radius: 14px;
                    text-align: left;
                    padding: 14px 18px;
                    font-size: 15px;
                    font-weight: 600;
                """)

            else:

                btn.setStyleSheet("""
                    background-color: transparent;
                    color: #cbd5e1;
                    border-radius: 14px;
                    text-align: left;
                    padding: 14px 18px;
                    font-size: 15px;
                    font-weight: 600;
                """)
