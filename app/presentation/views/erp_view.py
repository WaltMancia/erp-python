from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QStackedWidget
)

from app.presentation.components.sidebar import (
    Sidebar
)

from app.presentation.views.dashboard_view import (
    DashboardView
)

from app.presentation.views.product_view import (
    ProductView
)

from app.presentation.views.inventory_view import (
    InventoryView
)

from app.presentation.views.customer_view import (
    CustomerView
)

from app.presentation.views.sales_view import (
    SalesView
)

from app.presentation.views.sales_history_view import (
    SalesHistoryView
)


class ERPView(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        # ===== MAIN LAYOUT =====

        layout = QHBoxLayout()

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(0)

        # ===== SIDEBAR =====

        self.sidebar = Sidebar(self)

        # ===== STACK =====

        self.stack = QStackedWidget()

        # ===== VIEWS =====

        self.views = {

            "dashboard": DashboardView(),

            "products": ProductView(
                self.user
            ),

            "inventory": InventoryView(),

            "customers": CustomerView(),

            "sales": SalesView(),

            "sales_history": SalesHistoryView(),
        }

        # ===== ADD VIEWS TO STACK =====

        for view in self.views.values():

            self.stack.addWidget(view)

        # ===== LAYOUT =====

        layout.addWidget(self.sidebar)

        layout.addWidget(self.stack)

        self.setLayout(layout)

        # ===== DEFAULT PAGE =====

        self.switch_page(
            "dashboard"
        )

    def switch_page(
        self,
        page_name
    ):

        if page_name in self.views:

            self.stack.setCurrentWidget(
                self.views[page_name]
            )

            self.sidebar.set_active(
                page_name
            )
