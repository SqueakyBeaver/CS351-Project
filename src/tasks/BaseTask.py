# Abstract Base Class
import typing
from abc import ABC, abstractmethod

import mysql.connector as mysql


class BaseTask(ABC):
    def __init__(self, db_conn: mysql.MySQLConnection):
        self.db_conn = db_conn

    @abstractmethod
    def runTask(self, *args, **kwargs) -> typing.Any | None:
        pass
