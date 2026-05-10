from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFrame
)

from PySide6.QtCore import Qt

from app.application.usecases.auth_usecases import (
    login_user
)

from app.presentation.dialogs.register_dialog import (
    RegisterDialog
)

from app.core.exceptions import (
    AuthenticationError,
    DatabaseError
)


class LoginView(QWidget):

    def __init__(self, login_success_callback):
        super().__init__()

        self.login_success_callback = (
            login_success_callback
        )

        # Layout principal
        root_layout = QVBoxLayout()

        root_layout.setAlignment(Qt.AlignCenter)

        # Card
        card = QFrame()

        card.setObjectName("loginCard")

        card.setFixedWidth(400)

        card_layout = QVBoxLayout()

        card_layout.setSpacing(15)

        card_layout.setContentsMargins(
            30,
            30,
            30,
            30
        )

        # Título
        title = QLabel("ERP Login")

        title.setObjectName("loginTitle")

        title.setAlignment(Qt.AlignCenter)

        # Usuario
        self.username_input = QLineEdit()

        self.username_input.setPlaceholderText(
            "Usuario"
        )

        self.username_input.setMinimumHeight(40)

        # Password
        self.password_input = QLineEdit()

        self.password_input.setPlaceholderText(
            "Contraseña"
        )

        self.password_input.setEchoMode(
            QLineEdit.Password
        )

        self.password_input.setMinimumHeight(40)

        # Login button
        self.login_button = QPushButton(
            "Iniciar sesión"
        )

        self.login_button.setObjectName(
            "primary"
        )

        self.login_button.setMinimumHeight(42)

        self.login_button.clicked.connect(
            self.login
        )

        # Register button
        self.register_button = QPushButton(
            "Crear cuenta"
        )

        self.register_button.setObjectName(
            "secondary"
        )

        self.register_button.setMinimumHeight(40)

        self.register_button.clicked.connect(
            self.open_register
        )

        # Layout
        card_layout.addWidget(title)

        card_layout.addWidget(
            QLabel("Usuario")
        )

        card_layout.addWidget(
            self.username_input
        )

        card_layout.addWidget(
            QLabel("Contraseña")
        )

        card_layout.addWidget(
            self.password_input
        )

        card_layout.addSpacing(10)

        card_layout.addWidget(
            self.login_button
        )

        card_layout.addWidget(
            self.register_button
        )

        card.setLayout(card_layout)

        root_layout.addWidget(card)

        self.setLayout(root_layout)

    def login(self):

        username = (
            self.username_input.text().strip()
        )

        password = (
            self.password_input.text().strip()
        )

        try:

            user = login_user(
                username,
                password
            )

            QMessageBox.information(
                self,
                "Bienvenido",
                f"Hola {user.username}"
            )

            self.login_success_callback(user)

        except AuthenticationError as e:

            QMessageBox.warning(
                self,
                "Login",
                str(e)
            )

        except DatabaseError as e:

            QMessageBox.critical(
                self,
                "Base de datos",
                str(e)
            )

        except Exception:

            QMessageBox.critical(
                self,
                "Error",
                "Ha ocurrido un error inesperado"
            )

    def open_register(self):

        dialog = RegisterDialog()

        dialog.exec()
