from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QStackedWidget
)

from app.presentation.components.sidebar import (
    Sidebar
)

from app.presentation.views.product_view import (
    ProductView
)

from app.presentation.views.inventory_view import (
    InventoryView
)


class ERPView(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        layout = QHBoxLayout()

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(0)

        # ===== SIDEBAR =====

        self.sidebar = Sidebar(
            user,
            self.switch_view
        )

        # ===== STACK =====

        self.stack = QStackedWidget()

        # ===== VIEWS =====

        self.views = {

            "products": ProductView(
                self.user
            ),

            "inventory": InventoryView()
        }

        # ===== ADD TO STACK =====

        for view in self.views.values():

            self.stack.addWidget(view)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.setLayout(layout)

        # ===== DEFAULT ROUTE =====

        self.switch_view(
            "products"
        )

    def switch_view(self, route):

        view = self.views.get(route)

        if view:

            self.stack.setCurrentWidget(
                view
            )

            self.sidebar.set_active(
                route
            )
