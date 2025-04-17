import dbcfg

from .BaseTask import BaseTask


class ExampleTask(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, input):
        cursor = dbcfg.db_conn.cursor()  # Execute an SQL query
        # cursor.execute("")

        return "Pretend I did an SQL qury"
