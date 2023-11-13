from abc import ABC, abstractmethod


class Quackable(ABC):
    '''interface'''
    @abstractmethod
    def quack(self):
        pass


class MallardDuck(Quackable):
    def quack(self):
        print("꽥꽥")


class RedheadDuck(Quackable):
    def quack(self):
        print("꽥꽥")


class DuckCall(Quackable):
    def quack(self):
        print("꽉꽉")


class RubberDuck(Quackable):
    def quack(self):
        print("삑삑")


if __name__ == "__main__":
    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    duck_call = DuckCall()
    rubber_duck = RubberDuck()

    print("오리 시뮬레이션 게임")

    def simulate(duck):
        duck.quack()

    simulate(mallard_duck)
    simulate(redhead_duck)
    simulate(duck_call)
    simulate(rubber_duck)
