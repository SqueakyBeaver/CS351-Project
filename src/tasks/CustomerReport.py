from dataclasses import dataclass

from .BaseTask import BaseTask


@dataclass
class Item:
    description: str
    price_single: float
    num_ordered: int
    quoted_price: float


class CustomerReport(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, customer_name: str):
        if not customer_name:
            return (None, None)

        cursor = self.db_conn.cursor(buffered=True)

        # TODO: Add more information to reports?
        # Joins are overpowered, apparently
        cursor.execute(
            """
        SELECT ItemNum, NumOrdered, QuotedPrice FROM Orderline, Orders, Customer WHERE
        Orderline.orderNum = Orders.orderNum AND
        Orders.CustomerNum = Customer.CustomerNum AND
        Customer.CustomerName = (%s)
        """,
            params=[customer_name],
        )

        items: list[Item] = []
        for item_num, num_ordered, quoted_price in cursor.fetchall():
            cursor.execute(
                """
            SELECT Description, Price FROM Item WHERE ItemNum = %s
            """,
                params=[str(item_num)],
            )

            desc, single_price = cursor.fetchone()

            items.append(
                Item(desc, float(single_price), int(num_ordered), float(quoted_price))
            )

        total_price = sum(i.quoted_price for i in items)
        return (items, total_price)
