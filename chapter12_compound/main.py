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


class QuackCounter(Quackable):
    number_of_quacks = 0

    def __init__(self, duck):
        self.duck = duck  

    def quack(self):
        self.duck.quack()
        self.counter()

    @classmethod
    def counter(cls):
        cls.number_of_quacks += 1
        
    

if __name__ == "__main__":
    mallard_duck = QuackCounter(MallardDuck())
    redhead_duck = QuackCounter(RedheadDuck())
    duck_call = QuackCounter(DuckCall())
    rubber_duck = QuackCounter(RubberDuck())
    goose_duck = GooseAdapter(Goose())

    print("오리 시뮬레이션 게임")

    def simulate(duck):
        duck.quack()

    simulate(mallard_duck)
    simulate(redhead_duck)
    simulate(duck_call)
    simulate(rubber_duck)
    simulate(goose_duck)

    print("오리가 소리 낸 횟수 : {}번".format(QuackCounter.number_of_quacks))