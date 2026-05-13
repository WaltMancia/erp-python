import pandas as pd


class ExcelService:

    @staticmethod
    def export_products(
        products,
        filename="products.xlsx"
    ):

        data = []

        for p in products:

            data.append({
                "ID": p.id,
                "Nombre": p.name,
                "Precio": p.price,
                "Stock": p.stock
            })

        df = pd.DataFrame(data)

        df.to_excel(
            filename,
            index=False
        )

        return filename
