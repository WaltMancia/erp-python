from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QWidget
)

from PySide6.QtCore import Qt


class BaseDialog(QDialog):

    def __init__(
        self,
        title="Dialog"
    ):
        super().__init__()

        # ===== WINDOW =====

        self.setWindowTitle(title)

        self.setModal(True)

        self.resize(500, 350)

        self.setWindowFlag(
            Qt.FramelessWindowHint
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        # ===== MAIN LAYOUT =====

        outer_layout = QVBoxLayout()

        outer_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        # ===== CONTAINER =====

        self.container = QWidget()

        self.container.setObjectName(
            "dialogContainer"
        )

        self.layout = QVBoxLayout()

        self.layout.setSpacing(15)

        self.layout.setContentsMargins(
            25,
            25,
            25,
            25
        )

        # ===== TITLE =====

        title_label = QLabel(title)

        title_label.setObjectName(
            "dialogTitle"
        )

        self.layout.addWidget(
            title_label
        )

        self.container.setLayout(
            self.layout
        )

        outer_layout.addWidget(
            self.container
        )

        self.setLayout(
            outer_layout
        )
