from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import A4

from datetime import datetime


class PDFService:

    @staticmethod
    def export_products(
        products,
        filename="products_report.pdf"
    ):

        doc = SimpleDocTemplate(
            filename,
            pagesize=A4
        )

        elements = []

        styles = getSampleStyleSheet()

        title = Paragraph(
            "Reporte de Productos",
            styles["Title"]
        )

        elements.append(title)

        elements.append(
            Spacer(1, 20)
        )

        date = Paragraph(
            f"Generado: {datetime.now()}",
            styles["Normal"]
        )

        elements.append(date)

        elements.append(
            Spacer(1, 20)
        )

        data = [[
            "ID",
            "Nombre",
            "Precio",
            "Stock"
        ]]

        for p in products:

            data.append([
                p.id,
                p.name,
                f"Q{p.price:.2f}",
                p.stock
            ])

        table = Table(data)

        table.setStyle(TableStyle([
            (
                ("BACKGROUND"),
                (0, 0),
                (-1, 0),
                colors.HexColor("#2563eb")
            ),

            (
                ("TEXTCOLOR"),
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                ("GRID"),
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),

            (
                ("FONTNAME"),
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                ("BOTTOMPADDING"),
                (0, 0),
                (-1, 0),
                12
            )
        ]))

        elements.append(table)

        doc.build(elements)

        return filename
