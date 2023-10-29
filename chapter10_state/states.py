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
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("동전을 넣으셨습니다.")
        self.gumball_machine.state = self.has_quarter_state

    def eject_quarter(self):
        print("동전을 넣어주세요.")

    def trun_crank(self):
        print("동전을 넣어주세요.")

    def dispense(self):
        print("동전을 넣어주세요.")


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
