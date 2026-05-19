from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox
)


class BaseValidatedWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.layout.setSpacing(4)

        self.error_label = QLabel()

        self.error_label.setObjectName(
            "errorLabel"
        )

        self.error_label.hide()

        self.setLayout(
            self.layout
        )

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


class ValidatedLineEdit(
    BaseValidatedWidget
):

    def __init__(
        self,
        placeholder=""
    ):
        super().__init__()

        self.input = QLineEdit()

        self.input.setPlaceholderText(
            placeholder
        )

        self.layout.addWidget(
            self.input
        )

        self.layout.addWidget(
            self.error_label
        )

    def text(self):

        return self.input.text()

    def setText(self, value):

        self.input.setText(value)


class ValidatedSpinBox(
    BaseValidatedWidget
):

    def __init__(self):
        super().__init__()

        self.input = QSpinBox()

        self.layout.addWidget(
            self.input
        )

        self.layout.addWidget(
            self.error_label
        )

    def value(self):

        return self.input.value()

    def setValue(self, value):

        self.input.setValue(value)

    def setMaximum(self, value):

        self.input.setMaximum(value)


class ValidatedDoubleSpinBox(
    BaseValidatedWidget
):

    def __init__(self):
        super().__init__()

        self.input = QDoubleSpinBox()

        self.layout.addWidget(
            self.input
        )

        self.layout.addWidget(
            self.error_label
        )

    def value(self):

        return self.input.value()

    def setValue(self, value):

        self.input.setValue(value)

    def setMaximum(self, value):

        self.input.setMaximum(value)

    def setDecimals(self, value):

        self.input.setDecimals(value)

    def setPrefix(self, value):

        self.input.setPrefix(value)
