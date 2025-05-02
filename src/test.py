import unittest
from decimal import Decimal

import tasks
from dbcfg import _init_connection, _populate_db
from tasks.CustomerReport import Customer


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

        self.assertEqual(
            res,
            Customer(
                name="Toys Galore",
                total_ordered=Decimal("7"),
                total_quoted_price=Decimal("208.94"),
                num_orders=2,
                balance=Decimal("1210.25"),
                credit_limit=Decimal("7500.00"),
            ),
        )

        res = task.runTask("")
        self.assertIsNone(res)

        res = task.runTask("Construction Incorporated")
        print(f"{res=}")
        self.assertEqual(
            res,
            Customer(
                name="Construction Incorporated",
                total_ordered=None,
                total_quoted_price=None,
                num_orders=0,
                balance=None,
                credit_limit=None,
            ),
        )

    def test_login(self):
        task = tasks.Login(self.db_conn)
        res = task.runTask("FlippantCarp84", "supersecurepassword")
        self.assertTrue(res)

    def test_cr_lim(self):
        cursor = self.db_conn.cursor()
        task = tasks.CreditLimitUpdate(self.db_conn)
        res = task.runTask("Toys Galore", 9999.99)

    def test_rep_rep(self):
        cursor = self.db_conn.cursor()
        task = tasks.RepresentativeReport(self.db_conn)
        res = task.runTask()
        self.assertListEqual(
            res,
            [
                ("15", "Campos", "Rafael", 4, Decimal("2851.5875")),
                ("30", "Gradey", "Megan", 4, Decimal("1152.285")),
                ("45", "Tian", "Hui", 4, Decimal("1568.0625")),
                ("60", "Sefton", "Janet", 0, 0),
            ],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
