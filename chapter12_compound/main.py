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


class Goose:
    def honk(self):
        print("끽끽")


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose
    
    def quack(self):
        self.goose.honk()


if __name__ == "__main__":
    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    duck_call = DuckCall()
    rubber_duck = RubberDuck()
    goose_duck = GooseAdapter(Goose())

    print("오리 시뮬레이션 게임")

    def simulate(duck):
        duck.quack()

    simulate(mallard_duck)
    simulate(redhead_duck)
    simulate(duck_call)
    simulate(rubber_duck)
    simulate(goose_duck)
