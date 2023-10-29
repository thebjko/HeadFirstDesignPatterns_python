from enum import Enum


class State(Enum):
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3


class GumballMachine:
    state = State.SOLD_OUT

    def __init__(self, count):
        self.count = count
        if self.count > 0:
            self.state = State.NO_QUARTER

    def insert_quarter(self):
        match self.state:
            case State.HAS_QUARTER:
                print("동전은 한 개만 넣어 주세요.")
            case State.NO_QUARTER:
                self.state = State.HAS_QUARTER
                print("동전을 넣으셨습니다.")
            case State.SOLD_OUT:
                print("매진되었습니다. 다음 기회에 이용해주세요.")
            case State.SOLD:
                print("알맹이를 내보내고 있습니다.")
    
    def eject_quarter(self):
        match self.state:
            case State.HAS_QUARTER:
                print("동전이 반환됩니다.")
                self.state = State.NO_QUARTER
            case State.NO_QUARTER:
                print("동전을 넣어주세요.")
            case State.SOLD:
                print("이미 알맹이를 뽑으셨습니다.")
            case State.SOLD_OUT:
                print("동전을 넣지 않으셨습니다. 동전이 반환되지 않습니다.")
    
    def turn_crank(self):
        match self.state:
            case State.SOLD:
                print("손잡이는 한 번만 돌려주세요.")
            case State.NO_QUARTER:
                print("동전을 넣어 주세요.")
            case State.SOLD_OUT:
                print("매진되었습니다.")
            case State.HAS_QUARTER:
                print("손잡이를 돌리셨습니다.")
                self.state = State.SOLD
                self.dispense()

    def dispense(self):
        match self.state:
            case State.SOLD:
                print("알맹이를 내보내고 있습니다.")
                self.count -= 1
                if self.count == 0:
                    print("더이상 알맹이가 없습니다.")
                    self.state = State.SOLD_OUT
                else:
                    self.state = State.NO_QUARTER
            case State.NO_QUARTER:
                print("동전을 넣어주세요.")
            case State.SOLD_OUT:
                print("매진입니다.")
            case State.HAS_QUARTER:
                print("알맹이를 내보낼 수 있습니다.")

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
