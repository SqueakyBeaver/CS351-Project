# author: Camerik Baker
from .BaseTask import BaseTask


# Using UPDATE statement, alter a customer's Credit Limit if customer exists
class CreditLimitUpdate(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, customer_name: str, new_limit: float):
        if not customer_name or new_limit is None:
            return None

        cursor = self.db_conn.cursor()

        cursor.execute(
            "SELECT CreditLimit FROM Customer WHERE CustomerName = %s",
            params=[customer_name],
        )

        old_limit = float(cursor.fetchone())

        creditUpdate = "UPDATE Customer SET CreditLimit = %s WHERE CustomerName = %s"

        cursor.execute(
            creditUpdate,
            params=[new_limit, customer_name],
        )

        if cursor.fetchone():
            return (old_limit, new_limit)
        else:
            return (None, None)
