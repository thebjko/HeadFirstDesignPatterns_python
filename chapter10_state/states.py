from abc import ABC, abstractmethod


class State(ABC):
    """<< Interface >>"""
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def trun_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass
