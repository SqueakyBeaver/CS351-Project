class AddRepresentative:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def runTask(self, rep_num, first_name, last_name, street, city, state, postal_code, commission, rate):
        cursor = self.db_conn.cursor()

        query = """
        INSERT INTO rep (RepNum, LastName, FirstName, Street, City, State, PostalCode, Commission, Rate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (rep_num, last_name, first_name, street, city, state, postal_code, commission, rate))
        self.db_conn.commit()

        cursor.close()
