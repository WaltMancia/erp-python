import sys

from PySide6.QtWidgets import QApplication

from app.presentation.views.main_window import (
    MainWindow
)

from app.presentation.styles.theme import (
    get_stylesheet
)

app = QApplication(sys.argv)

# Styles
with open(
    "app/presentation/styles/style.qss",
    "r"
) as f:

    app.setStyleSheet(f.read())

window = MainWindow()

app.setStyleSheet(
    get_stylesheet()
)

window.show()

sys.exit(app.exec())
