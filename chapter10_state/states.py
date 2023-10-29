from abc import ABC, abstractmethod


class State(ABC):
    """<< Interface >>"""
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

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
        print("알맹이를 내보내고 있습니다.")

    def eject_quarter(self):
        print("이미 알맹이를 뽑으셨습니다.")

    def trun_crank(self):
        print("손잡이는 한 번만 돌려주세요.")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.state = self.gumball_machine.sold_out_state


class SoldOutState(State):
    def insert_quarter(self):
        print("sold out")

    def eject_quarter(self):
        print("sold out")

    def trun_crank(self):
        print("sold out")

    def dispense(self):
        print("sold out")


class NoQuarterState(State):
    # def __init__(self, gumball_machine):
    #     self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("동전을 넣으셨습니다.")
        self.gumball_machine.state = self.gumball_machine.has_quarter_state

    def eject_quarter(self):
        print("동전을 넣어주세요.")

    def trun_crank(self):
        print("동전을 넣어주세요.")

    def dispense(self):
        print("동전을 넣어주세요.")


class HasQuarterState(State):
    # def __init__(self, gumball_machine):
    #     self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("동전인 한 개만 넣어주세요.")

    def eject_quarter(self):
        print("동전이 반환됩니다.")
        self.gumball_machine.state = self.gumball_machine.no_quarter_state

    def trun_crank(self):
        print("손잡이를 돌리셨습니다.")
        self.gumball_machine.state = self.gumball_machine.sold_state

    def dispense(self):
        print("알맹이를 내보낼 수 없습니다.")



class WinnerState(State):
    def insert_quarter(self):
        return

    def eject_quarter(self):
        return

    def trun_crank(self):
        return

    def dispense(self):
        return
