from datetime import datetime

import argon2

from .BaseTask import BaseTask


class Login(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, userInput, passwordInput):
        cursor = self.db_conn.cursor()  # Execute an SQL query

        hasher = argon2.PasswordHasher()
        cursor.execute(
            "SELECT username, passwordHash FROM User WHERE username = %s",
            params=[userInput],
        )

        login_res = False
        for username, hash in cursor:
            login_res = hasher.verify(hash, passwordInput)

        if login_res:
            cursor.execute(
                "INSERT INTO Logins (username, loginTime) VALUES (%s, %s)",
                params=[userInput, datetime.now()],
            )

        return (login_res, userInput)


class Logout(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, username):
        cursor = self.db_conn.cursor()  # Execute an SQL query

        cursor.execute(
            "INSERT INTO Logouts (username, loginTime) VALUES (%s, %s)",
            params=[username, datetime.now()],
        )
