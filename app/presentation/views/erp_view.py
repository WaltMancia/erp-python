from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout
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

        self.sidebar = Sidebar(
            self.switch_view
        )

        self.product_view = ProductView()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.product_view)

        self.setLayout(layout)

    def switch_view(self, view_name):
        pass
