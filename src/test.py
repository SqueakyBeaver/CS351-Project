import unittest

import tasks
from dbcfg import _init_connection, _populate_db
from tasks.CustomerReport import Item


class TaskTest(unittest.TestCase):
    def setUp(self):
        # Populate the test database with clean data
        self.db_conn = _init_connection("351_group9_testing")
        _populate_db(self.db_conn)

    def tearDown(self):
        # Clear all the stuff in the test database
        cursor = self.db_conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS 351_group9_testing")
        self.db_conn.close()

    def test_customer_report(self):
        task = tasks.CustomerReport(self.db_conn)
        res = task.runTask("Toys Galore")

        self.assertTupleEqual(
            res,
            (
                [
                    Item(
                        description="Wood Block Set (48 piece)",
                        price_single=89.49,
                        num_ordered=5,
                        quoted_price=86.99,
                    ),
                    Item(
                        description="Rocking Horse",
                        price_single=124.95,
                        num_ordered=2,
                        quoted_price=121.95,
                    ),
                ],
                208.94,
            ),
        )

        res = task.runTask("")
        self.assertTupleEqual(res, (None, None))

        res = task.runTask("Construction Incorporated")
        self.assertTupleEqual(res, ([], 0))

    def test_login(self):
        task = tasks.Login(self.db_conn)
        res = task.runTask("FlippantCarp84", "supersecurepassword")
        self.assertTrue(res)

    def test_cr_lim(self):
        cursor = self.db_conn.cursor()
        task = tasks.CreditLimitUpdate(self.db_conn)
        res = task.runTask("Toys Galore", 9999.99)


if __name__ == "__main__":
    unittest.main(verbosity=2)
