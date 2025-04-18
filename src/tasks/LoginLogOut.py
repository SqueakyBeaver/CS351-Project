from .BaseTask import BaseTask
import argon2

class LoginLogOut(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def runTask(self, userInput, passwordInput):
        cursor = self.db_conn.cursor()  # Execute an SQL query
        
        hasher = argon2.PasswordHasher()
        cursor.execute(
            "SELECT username, passwordHash FROM User WHERE username = %s",
            params=[userInput],
        )

        for username, hash in cursor:
            return hasher.verify(hash, passwordInput)
            
