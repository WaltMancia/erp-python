from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget
)

from app.presentation.views.login_view import (
    LoginView
)

from app.presentation.views.erp_view import (
    ERPView
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python ERP")

        self.resize(1200, 700)

        self.stack = QStackedWidget()

        self.setCentralWidget(self.stack)

        # Login view
        self.login_view = LoginView(
            self.login_success
        )

        self.setObjectName(
            "mainContainer"
        )

        self.stack.addWidget(
            self.login_view
        )

    def login_success(self, user):

        self.erp_view = ERPView(user)

        self.stack.addWidget(
            self.erp_view
        )

        self.stack.setCurrentWidget(
            self.erp_view
        )
