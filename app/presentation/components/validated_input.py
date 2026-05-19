from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit
)


class ValidatedLineEdit(QWidget):

    def __init__(
        self,
        placeholder=""
    ):
        super().__init__()

        layout = QVBoxLayout()

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(4)

        self.input = QLineEdit()

        self.input.setPlaceholderText(
            placeholder
        )

        self.error_label = QLabel()

        self.error_label.setObjectName(
            "errorLabel"
        )

        self.error_label.hide()

        layout.addWidget(
            self.input
        )

        layout.addWidget(
            self.error_label
        )

        self.setLayout(layout)

    def text(self):

        return self.input.text()

    def setText(self, value):

        self.input.setText(value)

    def set_error(self, message):

        self.input.setObjectName(
            "inputError"
        )

        self.input.style().unpolish(
            self.input
        )

        self.input.style().polish(
            self.input
        )

        self.error_label.setText(
            message
        )

        self.error_label.show()

    def clear_error(self):

        self.input.setObjectName(
            ""
        )

        self.input.style().unpolish(
            self.input
        )

        self.input.style().polish(
            self.input
        )

        self.error_label.hide()
