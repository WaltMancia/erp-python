from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
    QHBoxLayout
)

from PySide6.QtCore import Qt

from app.application.usecases.product_usecases import (
    create_product,
    list_products,
    delete_product,
    update_product
)

from app.presentation.dialogs.product_dialog import ProductDialog


class ProductView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Espaciado profesional
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)

        # Botón crear producto
        self.add_button = QPushButton("Nuevo producto")
        self.add_button.setObjectName("primary")
        self.add_button.setMinimumHeight(40)

        self.add_button.clicked.connect(
            self.open_create_dialog
        )

        # Tabla
        self.table = QTableWidget()

        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels([
            "Nombre",
            "Precio",
            "Acciones"
        ])

        # Configuración PRO tabla
        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)

        self.table.setWordWrap(False)

        self.table.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        # Altura profesional filas
        self.table.verticalHeader().setDefaultSectionSize(60)

        # Altura mínima tabla
        self.table.setMinimumHeight(300)

        # Selección filas completas
        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        # Desactivar edición inline
        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        # Layout
        layout.addWidget(self.add_button)
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_products()

    def load_products(self):
        products = list_products()

        self.table.setRowCount(len(products))

        for row, p in enumerate(products):

            # Nombre
            self.table.setItem(
                row,
                0,
                QTableWidgetItem(p.name)
            )

            # Precio
            self.table.setItem(
                row,
                1,
                QTableWidgetItem(f"Q{p.price:.2f}")
            )

            # ===== BOTONES =====

            btn_layout = QHBoxLayout()

            btn_layout.setContentsMargins(
                5, 5, 5, 5
            )

            btn_layout.setSpacing(8)

            # Editar
            edit_btn = QPushButton("Editar")
            edit_btn.setObjectName("editBtn")
            edit_btn.setMinimumHeight(32)
            edit_btn.setCursor(Qt.PointingHandCursor)

            # Eliminar
            delete_btn = QPushButton("Eliminar")
            delete_btn.setObjectName("deleteBtn")
            delete_btn.setMinimumHeight(32)
            delete_btn.setCursor(Qt.PointingHandCursor)

            # Eventos
            edit_btn.clicked.connect(
                lambda _, p=p: self.edit_product(p)
            )

            delete_btn.clicked.connect(
                lambda _, p=p: self.delete_product_ui(p.id)
            )

            # Layout botones
            btn_layout.addWidget(edit_btn)
            btn_layout.addWidget(delete_btn)

            container = QWidget()
            container.setLayout(btn_layout)

            self.table.setCellWidget(
                row,
                2,
                container
            )

    def open_create_dialog(self):
        dialog = ProductDialog()

        if dialog.exec():

            data = dialog.get_data()

            create_product(
                data["name"],
                data["price"]
            )

            self.load_products()

    def edit_product(self, product):
        dialog = ProductDialog(product)

        if dialog.exec():

            data = dialog.get_data()

            update_product(
                product.id,
                data["name"],
                data["price"]
            )

            self.load_products()

    def delete_product_ui(self, product_id):

        confirm = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Deseas eliminar este producto?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:

            delete_product(product_id)

            self.load_products()
