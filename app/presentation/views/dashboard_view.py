from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QFrame,
    QSizePolicy
)

from PySide6.QtCharts import (
    QChart,
    QChartView,
    QPieSeries,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis
)

from PySide6.QtGui import (
    QPainter
)

from app.application.usecases.dashboard_usecases import (
    get_dashboard_stats,
    get_top_products
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

        main_layout = QVBoxLayout()

        title = QLabel(
            "Dashboard"
        )

        title.setObjectName(
            "pageTitle"
        )

        main_layout.addWidget(title)

        stats = get_dashboard_stats()

        # ===== KPI CARDS =====

        cards_layout = QGridLayout()

        cards_layout.addWidget(
            DashboardCard(
                "Productos",
                stats["products"]
            ),
            0,
            0
        )

        cards_layout.addWidget(
            DashboardCard(
                "Clientes",
                stats["customers"]
            ),
            0,
            1
        )

        cards_layout.addWidget(
            DashboardCard(
                "Ventas",
                stats["sales"]
            ),
            0,
            2
        )

        cards_layout.addWidget(
            DashboardCard(
                "Ingresos",
                f"Q{stats['revenue']:.2f}"
            ),
            1,
            0
        )

        cards_layout.addWidget(
            DashboardCard(
                "Stock Bajo",
                stats["low_stock"]
            ),
            1,
            1
        )

        main_layout.addLayout(
            cards_layout
        )

        # ===== TOP PRODUCTS CHART =====

        top_products = get_top_products()

        bar_set = QBarSet(
            "Vendidos"
        )

        categories = []

        for product_id, qty in top_products:

            categories.append(
                f"ID {product_id}"
            )

            bar_set.append(qty)

        series = QBarSeries()

        series.append(bar_set)

        chart = QChart()

        chart.addSeries(series)

        chart.setTitle(
            "Top Productos Vendidos"
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

        chart_view = QChartView(chart)

        chart_view.setRenderHint(
            QPainter.Antialiasing
        )

        chart_view.setMinimumHeight(
            350
        )

        chart_view.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        main_layout.addWidget(
            chart_view
        )

        self.setLayout(main_layout)
