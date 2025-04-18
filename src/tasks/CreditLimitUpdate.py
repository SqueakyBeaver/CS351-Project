# author: Camerik Baker
from .BaseTask import BaseTask

# Using UPDATE statement, alter a customer's Credit Limit if customer exists
class CreditLimitUpdate(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

    def runTask(self, customer_name: str) :
        if not customer_name:
            return(None, None)
        
        cursor = self.db_conn.cursor()

        creditUpdate = ('UPDATE Customer '
                        'SET CreditLimit = %s '
                        'WHERE CustomerName = %s')
        
        # must define a var "new_limit" to hold customer's updated credit limit val. 
        # New value should be based on user input
        # params line will remain commented out until var is def and init
        cursor.execute(
            creditUpdate,
            #params=[new_limit ,customer_name],
        )