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


class ERPView(QWidget):

    def __init__(self, user):
        super().__init__()

        self.user = user

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar(
            user,
            self.switch_view
        )

        # Stack
        self.stack = QStackedWidget()

        self.product_view = ProductView(
            self.user
        )

        self.stack.addWidget(
            self.product_view
        )

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.setLayout(layout)

    def switch_view(self, view_name):

        if view_name == "products":

            self.stack.setCurrentWidget(
                self.product_view
            )
