# author: Camerik Baker
from .BaseTask import BaseTask

# Using UPDATE statement, alter a customer's Credit Limit if customer exists
class CreditLimitUpdate(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

    def runTask(self, customer_name: str, new_limit: float) :
        if not customer_name or new_limit is None :
            return None
        
        cursor = self.db_conn.cursor()

        old_limit = (' SELECT CreditLimit '
                  ' FROM Customer')

        creditUpdate = ('UPDATE Customer '
                        'SET CreditLimit = %s '
                        'WHERE CustomerName = %s')
        

        cursor.execute(
            creditUpdate,
            params=[new_limit ,customer_name],
        )

    # add a print statement to verify completion of task
    # 'credit limit for user "[user]" updated from [oldLim] to [newLim]'
        if cursor.fetchone():
            return (f"Credit Limit for User '{customer_name}'"
            f"successfully updated from {old_limit} to {new_limit}")
        else:
            return "Could not update Credit Limit."

