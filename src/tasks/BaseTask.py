# Abstract Base Class
import typing
import mysql.connector as mysql
from abc import ABC, abstractmethod


class BaseTask(ABC):
    def __init__(self, db_conn: mysql.MySQLConnection):
        """
        Constructor
        Not really necessary tbh, but putting it here just in case we need it
        """
        self.db_conn = db_conn

    @abstractmethod
    def runTask(self, *args, **kwargs) -> typing.Any | None:
        pass
