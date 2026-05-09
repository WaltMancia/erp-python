from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from app.application.usecases.auth_usecases import (
    register_user
)


class RegisterDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crear cuenta")
        self.setMinimumWidth(350)

        layout = QVBoxLayout()

        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        # Usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText(
            "Usuario"
        )

        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText(
            "Contraseña"
        )

        self.password_input.setEchoMode(
            QLineEdit.Password
        )

        # Botón
        self.register_button = QPushButton(
            "Crear cuenta"
        )

        self.register_button.setObjectName(
            "primary"
        )

        self.register_button.setMinimumHeight(40)

        self.register_button.clicked.connect(
            self.register
        )

        # Layout
        layout.addWidget(QLabel("Usuario"))
        layout.addWidget(self.username_input)

        layout.addWidget(QLabel("Contraseña"))
        layout.addWidget(self.password_input)

        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):

        username = self.username_input.text().strip()

        password = self.password_input.text().strip()

        try:

            register_user(
                username,
                password
            )

            QMessageBox.information(
                self,
                "Éxito",
                "Cuenta creada correctamente"
            )

            self.accept()

        except ValueError as e:

            QMessageBox.warning(
                self,
                "Validación",
                str(e)
            )
