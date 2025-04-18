import argon2
import unittest
import tasks
from dbcfg import _init_connection, _populate_db


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

        self.assertTupleEqual(res, ("Toys Galore", 208.94))

        res = task.runTask("")
        self.assertTupleEqual(res, (None, None))

        res = task.runTask("Your mother")
        self.assertTupleEqual(res, ("Your mother", 0))

    def test_login(self):
        cursor = self.db_conn.cursor()
        hasher = argon2.PasswordHasher()

        cursor.execute(
            "SELECT username, passwordHash FROM User WHERE username = (%s)",
            params=["FlippantCarp84"],
        )

        for username, hash in cursor:
            self.assertTrue(
                hasher.verify(str(hash), "supersecurepassword")
            )
            self.assertEqual(username, "FlippantCarp84")


if __name__ == "__main__":
    unittest.main(verbosity=2)
