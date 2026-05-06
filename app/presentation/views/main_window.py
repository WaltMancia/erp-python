from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedWidget
from app.presentation.components.sidebar import Sidebar
from app.presentation.views.product_view import ProductView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ERP System")
        self.resize(900, 500)

        layout = QHBoxLayout()

        # Sidebar
        self.sidebar = Sidebar(self.switch_view)

        # Área de contenido
        self.stack = QStackedWidget()

        # Vistas
        self.product_view = ProductView()

        self.stack.addWidget(self.product_view)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.setLayout(layout)

    def switch_view(self, view_name):
        if view_name == "products":
            self.stack.setCurrentWidget(self.product_view)