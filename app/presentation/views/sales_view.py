from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


class SalesView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel(
            "Módulo de Ventas"
        )

        title.setObjectName(
            "pageTitle"
        )

        layout.addWidget(title)

        self.setLayout(layout)
