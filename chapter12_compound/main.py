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
        

class AbstractDuckFactory(ABC):
    @abstractmethod
    def create_mallard_duck(self):
        pass

    @abstractmethod
    def create_redhead_duck(self):
        pass

    @abstractmethod
    def create_duck_call(self):
        pass

    @abstractmethod
    def create_rubber_duck(self):
        pass


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()
    
    def create_redhead_duck(self):
        return RedheadDuck()
    
    def create_duck_call(self):
        return DuckCall()
    
    def create_rubber_duck(self):
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())
    
    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())
    
    def create_duck_call(self):
        return QuackCounter(DuckCall())
    
    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())


class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()


if __name__ == "__main__":
    duck_factory = CountingDuckFactory()
    mallard_duck = duck_factory.create_mallard_duck()
    redhead_duck = duck_factory.create_redhead_duck()
    duck_call = duck_factory.create_duck_call()
    rubber_duck = duck_factory.create_rubber_duck()
    goose_duck = GooseAdapter(Goose())

    print("오리 시뮬레이션 게임: 무리 (+컴포지트)")

    flock_of_ducks = Flock()

    flock_of_ducks.add(redhead_duck)
    flock_of_ducks.add(duck_call)
    flock_of_ducks.add(rubber_duck)
    flock_of_ducks.add(goose_duck)

    flock_of_mallards = Flock()
    mallard_one = duck_factory.create_mallard_duck()
    mallard_two = duck_factory.create_mallard_duck()
    mallard_three = duck_factory.create_mallard_duck()
    mallard_four = duck_factory.create_mallard_duck()

    flock_of_mallards.add(mallard_one)
    flock_of_mallards.add(mallard_two)
    flock_of_mallards.add(mallard_three)
    flock_of_mallards.add(mallard_four)

    flock_of_ducks.add(flock_of_mallards)

    def simulate(duck):
        duck.quack()

    print("오리 시뮬레이션 게임: 전체 무리")
    simulate(flock_of_ducks)

    print("오리 시뮬레이션 게임: 물오리 무리")
    simulate(flock_of_mallards)

    print("오리가 소리 낸 횟수 : {}번".format(QuackCounter.number_of_quacks))
