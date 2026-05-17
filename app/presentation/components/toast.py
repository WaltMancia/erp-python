from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout
)

from PySide6.QtCore import (
    QTimer,
    QPropertyAnimation,
    QEasingCurve
)


class Toast(QFrame):

    def __init__(
        self,
        parent,
        message,
        toast_type="success"
    ):
        super().__init__(parent)

        self.setObjectName(
            f"toast-{toast_type}"
        )

        self.setFixedHeight(55)

        self.setMinimumWidth(320)

        layout = QHBoxLayout()

        self.label = QLabel(message)

        layout.addWidget(self.label)

        self.setLayout(layout)

        # ===== POSITION =====

        self.move(
            parent.width() - 360,
            30
        )

        # ===== ANIMATION =====

        self.animation = QPropertyAnimation(
            self,
            b"windowOpacity"
        )

        self.animation.setDuration(300)

        self.animation.setStartValue(0)

        self.animation.setEndValue(1)

        self.animation.setEasingCurve(
            QEasingCurve.OutCubic
        )

        self.animation.start()

        self.show()

        # ===== AUTO CLOSE =====

        QTimer.singleShot(
            3000,
            self.close_toast
        )

    def close_toast(self):

        self.fade_out = QPropertyAnimation(
            self,
            b"windowOpacity"
        )

        self.fade_out.setDuration(300)

        self.fade_out.setStartValue(1)

        self.fade_out.setEndValue(0)

        self.fade_out.finished.connect(
            self.close
        )

        self.fade_out.start()
