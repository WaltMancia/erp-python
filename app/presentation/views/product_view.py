from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
    QHBoxLayout
)

from PySide6.QtWidgets import QFileDialog

from app.presentation.components.toast import (
    Toast
)

from app.services.pdf_service import (
    PDFService
)

from app.services.excel_service import (
    ExcelService
)

from PySide6.QtCore import Qt
from app.core.permissions import (
    has_permission
)
from app.application.usecases.product_usecases import (
    create_product,
    list_products,
    delete_product,
    update_product
)

from app.presentation.dialogs.product_dialog import ProductDialog


class ProductView(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
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

        self.pdf_button = QPushButton(
            "Exportar PDF"
        )

        self.excel_button = QPushButton(
            "Exportar Excel"
        )

        self.pdf_button.clicked.connect(
            self.export_pdf
        )

        self.excel_button.clicked.connect(
            self.export_excel
        )

        # Tabla
        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Nombre",
            "Precio",
            "Stock",
            "Estado",
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
            3,
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
        if has_permission(
            self.user,
            "products.create"
        ):
            toolbar = QHBoxLayout()

            toolbar.addWidget(self.add_button)
            toolbar.addWidget(self.pdf_button)
            toolbar.addWidget(self.excel_button)

            toolbar.addStretch()

            layout.addLayout(toolbar)

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

            # Stock
            self.table.setItem(
                row,
                2,
                QTableWidgetItem(str(p.stock))
            )

            status = QLabel()

            if p.stock <= 5:

                status.setText("Stock Bajo")

                status.setStyleSheet("""
                    background:#7f1d1d;
                    color:white;
                    padding:6px 12px;
                    border-radius:8px;
                """)

            else:

                status.setText("Disponible")

                status.setStyleSheet("""
                    background:#14532d;
                    color:white;
                    padding:6px 12px;
                    border-radius:8px;
                """)

            status.setAlignment(Qt.AlignCenter)

            self.table.setCellWidget(
                row,
                3,
                status
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
            if has_permission(
                self.user,
                "products.edit"
            ):
                btn_layout.addWidget(edit_btn)

            if has_permission(
                self.user,
                "products.delete"
            ):
                btn_layout.addWidget(delete_btn)

            container = QWidget()
            container.setLayout(btn_layout)

            self.table.setCellWidget(
                row,
                4,
                container
            )

    def open_create_dialog(self):
        dialog = ProductDialog()

        if dialog.exec():

            data = dialog.get_data()

            create_product(
                data["name"],
                data["price"],
                data["stock"]
            )

            self.load_products()

    def edit_product(self, product):
        dialog = ProductDialog(product)

        if dialog.exec():

            data = dialog.get_data()

            update_product(
                product.id,
                data["name"],
                data["price"],
                data["stock"]
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

    def export_pdf(self):

        products = list_products()

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF",
            "productos.pdf",
            "PDF Files (*.pdf)"
        )

        if filename:

            PDFService.export_products(
                products,
                filename
            )

            Toast(
                self,
                "Éxito",
                "PDF exportado correctamente"
            )

    def export_excel(self):

        products = list_products()

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Excel",
            "productos.xlsx",
            "Excel Files (*.xlsx)"
        )

        if filename:

            ExcelService.export_products(
                products,
                filename
            )

            Toast(
                self,
                "Éxito",
                "Excel exportado correctamente"
            )
