from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QFrame,
    QListWidget,
    QListWidgetItem
)

from app.application.usecases.dashboard_usecases import (
    get_dashboard_metrics
)


class DashboardCard(QFrame):

    def __init__(
        self,
        title,
        value
    ):
        super().__init__()

        self.setObjectName(
            "dashboardCard"
        )

        layout = QVBoxLayout()

        title_label = QLabel(title)

        title_label.setObjectName(
            "dashboardCardTitle"
        )

        value_label = QLabel(
            str(value)
        )

        value_label.setObjectName(
            "dashboardCardValue"
        )

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        self.setLayout(layout)


class DashboardView(QWidget):

    def __init__(self):
        super().__init__()

        metrics = get_dashboard_metrics()

        main_layout = QVBoxLayout()

        # ===== TITLE =====

        title = QLabel(
            "Dashboard"
        )

        title.setObjectName(
            "pageTitle"
        )

        main_layout.addWidget(title)

        # ===== KPI GRID =====

        grid = QGridLayout()

        grid.setSpacing(20)

        grid.addWidget(
            DashboardCard(
                "Productos",
                metrics["total_products"]
            ),
            0,
            0
        )

        grid.addWidget(
            DashboardCard(
                "Stock Bajo",
                metrics["low_stock"]
            ),
            0,
            1
        )

        grid.addWidget(
            DashboardCard(
                "Ventas",
                metrics["total_sales"]
            ),
            1,
            0
        )

        grid.addWidget(
            DashboardCard(
                "Ingresos",
                f"Q{metrics['revenue']:.2f}"
            ),
            1,
            1
        )

        main_layout.addLayout(grid)

        # ===== RECENT ACTIVITY =====

        activity_title = QLabel(
            "Actividad reciente"
        )

        activity_title.setObjectName(
            "sectionTitle"
        )

        main_layout.addWidget(
            activity_title
        )

        activity_list = QListWidget()

        for movement in metrics[
            "recent_movements"
        ]:

            item = QListWidgetItem(
                f"{movement.type} | "
                f"Producto ID {movement.product_id} | "
                f"Cantidad: {movement.quantity}"
            )

            activity_list.addItem(item)

        main_layout.addWidget(
            activity_list
        )

        self.setLayout(main_layout)
