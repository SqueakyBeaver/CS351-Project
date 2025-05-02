from dataclasses import asdict, dataclass
from decimal import Decimal

from .BaseTask import BaseTask


@dataclass
class Customer:
    name: str
    total_ordered: int
    total_quoted_price: Decimal
    num_orders: int
    balance: Decimal
    credit_limit: Decimal


class CustomerReport(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, customer_name: str) -> Customer | None:
        if not customer_name:
            return None

        cursor = self.db_conn.cursor(buffered=True)

        cursor.execute(
            """
        SELECT CustomerName, SUM(NumOrdered), SUM(QuotedPrice), 
        COUNT(Orders.orderNum), Balance, CreditLimit
        FROM Orderline, Orders, Customer
        WHERE Orderline.orderNum = Orders.orderNum
        AND Orders.CustomerNum = Customer.CustomerNum
        AND Customer.CustomerName = (%s)
        """,
            params=[customer_name],
        )

        items = [list(i) for i in cursor.fetchall()]
        # If there's duplicate entries for customers, then we should probably merge them
        final_res = Customer(*items.pop(0))

        # Reducing calls/improving readability(ish)
        customer_fields = list(asdict(final_res))

        for row in items:
            for idx, i in enumerate(row):
                setattr(final_res, customer_fields[idx], i)

        return final_res
