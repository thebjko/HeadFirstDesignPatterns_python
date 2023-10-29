from enum import Enum
from states import *

class State(Enum):
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3


class GumballMachine:
    state = State.SOLD_OUT

    def __init__(self, number_gumballs):
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)

        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()
    
    def eject_quarter(self):
        self.state.eject_quarter()
    
    def turn_crank(self):
        self.state.trun_crank()

    def dispense(self):
        self.state.dispense()

    def release_ball(self):
        print("알맹이를 내보내고 있습니다.")
        if self.count > 0:
            self.count -= 1

    def __str__(self):
        return f"State: {self.state}"


def gumball_machine_test_drive():
    gumball_machine = GumballMachine(5)

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.eject_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.eject_quarter()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)


if __name__ == "__main__":
    gumball_machine_test_drive()
