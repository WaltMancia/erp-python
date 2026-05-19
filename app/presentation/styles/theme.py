GLOBAL_STYLE = """
/* =========================================================
   GLOBAL
========================================================= */

QWidget {
    background-color: #0f172a;
    color: #f8fafc;
    font-family: 'Segoe UI';
    font-size: 14px;
}


/* =========================================================
   MAIN WINDOW
========================================================= */

#mainContainer {
    background-color: #0f172a;
}


/* =========================================================
   SIDEBAR
========================================================= */

#sidebar {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

#logoText {
    font-size: 20px;
    font-weight: bold;
    color: white;
    padding: 10px 0;
}

.sidebarButton {
    text-align: left;
    padding: 14px 18px;
    border-radius: 14px;
    border: none;
    background-color: transparent;
    font-size: 15px;
    font-weight: 600;
    color: #cbd5e1;
}

.sidebarButton:hover {
    background-color: #172554;
    color: white;
}

.sidebarButtonActive {
    background-color: #2563eb;
    color: white;
}

.sidebarButtonActive:hover {
    background-color: #2563eb;
}


/* =========================================================
   TABLES
========================================================= */

QTableWidget {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    gridline-color: #334155;
    padding: 10px;
}

QHeaderView::section {
    background-color: #2563eb;
    color: white;
    border: none;
    padding: 14px;
    font-size: 15px;
    font-weight: bold;
}

QTableWidget::item {
    padding: 12px;
    border-bottom: 1px solid #334155;
}

QTableWidget::item:selected {
    background-color: #1d4ed8;
}


/* =========================================================
   BUTTONS
========================================================= */

QPushButton {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 12px 18px;
    color: white;
    font-weight: 600;
    min-height: 18px;
}

QPushButton:hover {
    background-color: #334155;
}

QPushButton:pressed {
    background-color: #475569;
}


/* PRIMARY BUTTON */

QPushButton#primary {
    background-color: #2563eb;
    border: none;
}

QPushButton#primary:hover {
    background-color: #1d4ed8;
}


/* EDIT BUTTON */

QPushButton#editBtn {
    background-color: #f59e0b;
    color: white;
    min-width: 110px;
    font-weight: bold;
}

QPushButton#editBtn:hover {
    background-color: #d97706;
}


/* DELETE BUTTON */

QPushButton#deleteBtn {
    background-color: #ef4444;
    color: white;
    min-width: 110px;
    font-weight: bold;
}

QPushButton#deleteBtn:hover {
    background-color: #dc2626;
}


/* EXPORT BUTTONS */

QPushButton#pdfBtn {
    background-color: #1e293b;
}

QPushButton#excelBtn {
    background-color: #166534;
}

QPushButton#excelBtn:hover {
    background-color: #15803d;
}


/* =========================================================
   INPUTS
========================================================= */

QLineEdit,
QSpinBox,
QDoubleSpinBox,
QComboBox {
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 10px;
    min-height: 18px;
    color: white;
}

QLineEdit:focus,
QSpinBox:focus,
QDoubleSpinBox:focus,
QComboBox:focus {
    border: 1px solid #2563eb;
}


/* =========================================================
   DIALOGS
========================================================= */

#dialogContainer {
    background-color: #111827;
    border-radius: 18px;
    border: 1px solid #334155;
}

#dialogTitle {
    font-size: 24px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}


/* =========================================================
   VALIDATION
========================================================= */

#errorLabel {
    color: #ef4444;
    font-size: 12px;
    padding-left: 4px;
}

#inputError {
    border: 1px solid #ef4444;
}


/* =========================================================
   BADGES
========================================================= */

#successBadge {
    background-color: #166534;
    color: white;
    border-radius: 10px;
    padding: 6px 12px;
    font-weight: bold;
}


/* =========================================================
   SCROLLBAR
========================================================= */

QScrollBar:vertical {
    border: none;
    background: #0f172a;
    width: 10px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: #334155;
    border-radius: 5px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: #475569;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0;
}
"""
