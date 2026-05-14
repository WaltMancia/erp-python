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


class TicketService:

    @staticmethod
    def generate_ticket(
        sale,
        items,
        filename
    ):

        doc = SimpleDocTemplate(
            filename,
            pagesize=A4
        )

        styles = getSampleStyleSheet()

        elements = []

        # ===== TITLE =====

        title = Paragraph(
            "ERP PYTHON - FACTURA",
            styles["Title"]
        )

        elements.append(title)

        elements.append(
            Spacer(1, 20)
        )

        # ===== INFO =====

        info = Paragraph(
            f"""
            Venta ID: {sale.id}<br/>
            Fecha: {sale.created_at}<br/>
            """,
            styles["Normal"]
        )

        elements.append(info)

        elements.append(
            Spacer(1, 20)
        )

        # ===== TABLE =====

        data = [[
            "Producto",
            "Cantidad",
            "Precio",
            "Subtotal"
        ]]

        total = 0

        for item in items:

            subtotal = (
                item.price *
                item.quantity
            )

            total += subtotal

            data.append([
                str(item.product_id),
                item.quantity,
                f"Q{item.price:.2f}",
                f"Q{subtotal:.2f}"
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
            ),

            (
                ("GRID"),
                (0, 0),
                (-1, -1),
                1,
                colors.black
            )
        ]))

        elements.append(table)

        elements.append(
            Spacer(1, 20)
        )

        # ===== TOTAL =====

        total_paragraph = Paragraph(
            f"<b>Total: Q{total:.2f}</b>",
            styles["Heading2"]
        )

        elements.append(
            total_paragraph
        )

        doc.build(elements)
