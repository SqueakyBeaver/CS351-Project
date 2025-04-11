# Abstract Base Class
import typing
from abc import ABC, abstractmethod


class BaseTask(ABC):
    def __init__(self):
        """
        Constructor
        Not really necessary tbh, but putting it here just in case we need it
        """
        pass

    @abstractmethod
    def runTask(self, *args, **kwargs) -> typing.Any | None:
        pass
