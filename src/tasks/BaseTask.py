# Abstract Base Class
import typing
from abc import ABC, abstractmethod
from mysql.connector.connection import MySQLConnection

class BaseTask(ABC):
    def __init__(self, dbConn: MySQLConnection):
        """Constructor: pass a dbConn that is the mySQL connection"""
        self.dbConn = dbConn

    @abstractmethod
    def runTask(self, *args, **kwargs) -> typing.Any | None:
        pass


