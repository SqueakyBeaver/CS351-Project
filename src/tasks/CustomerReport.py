from .BaseTask import BaseTask


class CustomerReport(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, customer_name: str):
        if not customer_name:
            return (None, None)

        cursor = self.db_conn.cursor()

        # TODO: Add more information to reports?
        # Joins are overpowered, apparently
        cursor.execute(
            """
        SELECT QuotedPrice FROM Orderline, Orders, Customer WHERE
        Orderline.orderNum = Orders.orderNum AND
        Orders.CustomerNum = Customer.CustomerNum AND
        Customer.CustomerName = (%s)
        """,
            params=[customer_name],
        )

        try:
            total_price = sum([float(i[0]) for i in cursor])
        except TypeError:
            # Malformed data probably (the price is not a float)
            pass

        return (customer_name, total_price)
