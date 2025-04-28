from .BaseTask import BaseTask


class RepresentativeReport(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self):
        cursor = self.db_conn.cursor()  # Execute an SQL query
        cursor.execute("""
        SELECT RepNum, LastName, FirstName
        FROM Rep               
        """)
        reps = cursor.fetchall()
        res = []
        for RepNum, LastName, FirstName in reps:
            cursor.execute("""
            SELECT Balance
            FROM Customer
            WHERE RepNum = %s                              
            """, params = [RepNum])
            customers = cursor.fetchall()
            sum = 0
            for i in customers:
                sum += i[0]
            if customers:
                res.append((RepNum, LastName, FirstName, len(customers), sum/len(customers)))
            else:
                res.append((RepNum, LastName, FirstName, len(customers), 0))
        return res