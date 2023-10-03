from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print('quack')
    
    def fly(self):
        print('fly')


class Turkey(metaclass=ABCMeta):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print('골골')

    def fly(self):
        print('short distance fly')


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


if __name__ == '__main__':
    duck = MallardDuck()
    turkey = WildTurkey()

    turkey_adapter = TurkeyAdapter(turkey)

    turkey.gobble()
    turkey.fly()

    def test_duck(duck: Duck):
        duck.quack()
        duck.fly()

    print('Test Duck')
    test_duck(duck)

    print('Test TurkeyAdapter')
    test_duck(turkey_adapter)


