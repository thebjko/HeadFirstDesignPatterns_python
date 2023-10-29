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


class SoldState(State):
    def insert_quarter(self):
        return

    def eject_quarter(self):
        return

    def trun_crank(self):
        return

    def dispense(self):
        return


class SoldOutState(State):
    def insert_quarter(self):
        return

    def eject_quarter(self):
        return

    def trun_crank(self):
        return

    def dispense(self):
        return


class NoQuarterState(State):
    def insert_quarter(self):
        return

    def eject_quarter(self):
        return

    def trun_crank(self):
        return

    def dispense(self):
        return


class HasQuarterState(State):
    def insert_quarter(self):
        return

    def eject_quarter(self):
        return

    def trun_crank(self):
        return

    def dispense(self):
        return



class WinnerState(State):
    def insert_quarter(self):
        return

    def eject_quarter(self):
        return

    def trun_crank(self):
        return

    def dispense(self):
        return
