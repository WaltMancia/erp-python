from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QFrame,
    QListWidget,
    QListWidgetItem
)

from PySide6.QtCharts import (
    QChart,
    QChartView,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis
)

from PySide6.QtGui import (
    QPainter
)

from app.application.usecases.dashboard_usecases import (
    get_dashboard_metrics
)

from app.application.usecases.analytics_usecases import (
    sales_by_day,
    low_stock_products
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

        # ===== SALES CHART =====

        chart_title = QLabel(
            "Ventas por día"
        )

        chart_title.setObjectName(
            "sectionTitle"
        )

        main_layout.addWidget(
            chart_title
        )

        sales_data = sales_by_day()

        categories = []

        bar_set = QBarSet(
            "Ventas"
        )

        for date, total in sales_data:

            categories.append(
                str(date)
            )

            bar_set.append(
                float(total)
            )

        series = QBarSeries()

        series.append(bar_set)

        chart = QChart()

        chart.addSeries(series)

        chart.setTitle(
            "Ingresos diarios"
        )

        chart.setAnimationOptions(
            QChart.SeriesAnimations
        )

        axis = QBarCategoryAxis()

        axis.append(categories)

        chart.createDefaultAxes()

        chart.setAxisX(
            axis,
            series
        )

        chart.legend().setVisible(
            True
        )

        chart_view = QChartView(chart)

        chart_view.setRenderHint(
            QPainter.Antialiasing
        )

        chart_view.setMinimumHeight(
            350
        )

        main_layout.addWidget(
            chart_view
        )

        # ===== LOW STOCK =====

        low_stock_title = QLabel(
            "Productos con stock bajo"
        )

        low_stock_title.setObjectName(
            "sectionTitle"
        )

        main_layout.addWidget(
            low_stock_title
        )

        low_stock_list = QListWidget()

        for product in low_stock_products():

            item = QListWidgetItem(
                f"{product.name} | Stock: {product.stock}"
            )

            low_stock_list.addItem(item)

        main_layout.addWidget(
            low_stock_list
        )

        self.setLayout(main_layout)
