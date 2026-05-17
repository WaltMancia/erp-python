def get_stylesheet():

    return """
    
    QWidget {
        background-color: #0f172a;
        color: white;
        font-size: 14px;
        font-family: Segoe UI;
    }

    /* ===== PAGE TITLES ===== */

    #pageTitle {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 15px;
        color: white;
    }

    /* ===== BUTTONS ===== */

    QPushButton {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 10px 16px;
        color: white;
        font-weight: 600;
    }

    QPushButton:hover {
        background-color: #334155;
    }

    QPushButton:pressed {
        background-color: #475569;
    }

    QPushButton#primary {
        background-color: #2563eb;
        border: none;
    }

    QPushButton#primary:hover {
        background-color: #3b82f6;
    }

    QPushButton#deleteBtn {
        background-color: #dc2626;
        border: none;
    }

    QPushButton#deleteBtn:hover {
        background-color: #ef4444;
    }

    QPushButton#editBtn {
        background-color: #f59e0b;
        border: none;
        color: black;
    }

    QPushButton#editBtn:hover {
        background-color: #fbbf24;
    }

    /* ===== TABLES ===== */

    QTableWidget {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        gridline-color: #334155;
        padding: 10px;
    }

    QHeaderView::section {
        background-color: #2563eb;
        color: white;
        padding: 12px;
        border: none;
        font-weight: bold;
    }

    QTableWidget::item {
        padding: 10px;
    }

    QTableWidget::item:selected {
        background-color: #3b82f6;
    }

    /* ===== INPUTS ===== */

    QLineEdit,
    QComboBox,
    QSpinBox,
    QTextEdit {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 8px;
        color: white;
    }

    QLineEdit:focus,
    QComboBox:focus,
    QSpinBox:focus,
    QTextEdit:focus {
        border: 1px solid #3b82f6;
    }

    /* ===== SIDEBAR ===== */

    #sidebar {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }

    #sidebarButton {
        text-align: left;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 6px;
    }

    #sidebarButton:hover {
        background-color: #1e293b;
    }

    #sidebarButtonActive {
        background-color: #2563eb;
        color: white;
    }

    /* ===== DASHBOARD ===== */

    #dashboardCard {
        background-color: #1e293b;
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #334155;
    }

    #dashboardCard:hover {
        border: 1px solid #3b82f6;
    }

    #dashboardCardTitle {
        font-size: 14px;
        color: #94a3b8;
    }

    #dashboardCardValue {
        font-size: 28px;
        font-weight: bold;
        color: white;
    }

    /* ===== SCROLLBAR ===== */

    QScrollBar:vertical {
        border: none;
        background: #0f172a;
        width: 10px;
        margin: 0;
    }

    QScrollBar::handle:vertical {
        background: #334155;
        border-radius: 5px;
    }

    QScrollBar::handle:vertical:hover {
        background: #475569;
    }
    
    /* ===== SIDEBAR ===== */

    #sidebar {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }

    #sidebarLogo {
        font-size: 24px;
        font-weight: bold;
        padding: 20px;
        color: white;
    }

    #sidebarButton {
        text-align: left;
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 6px;
        background-color: transparent;
        border: none;
        font-size: 15px;
    }

    #sidebarButton:hover {
        background-color: #1e293b;
    }

    #sidebarButtonActive {
        text-align: left;
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 6px;
        background-color: #2563eb;
        border: none;
        font-size: 15px;
        color: white;
    }

    """
