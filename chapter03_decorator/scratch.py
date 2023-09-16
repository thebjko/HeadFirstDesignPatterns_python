from abc import ABC, abstractmethod
from sys import argv
from math import fsum


class Beverage(ABC):
    description = '제목 없음'

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    # @property
    # @abstractmethod
    # def milk(self):
    #     pass

    # @milk.setter
    # @abstractmethod
    # def milk(self, val):
    #     pass

    # @property
    # @abstractmethod
    # def whip(self):
    #     pass

    # @whip.setter
    # @abstractmethod
    # def whip(self):
    #     pass


class CondimentDecorator(Beverage):
    beverage: Beverage

    @abstractmethod
    def description(self):
        pass

class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self):
        return .89


class GuatemalaAntigua(Beverage):
    def __init__(self):
        self.description = 'Guatemala Antigua Coffee : Chocolatey'

    def cost(self):
        return 1.29
    

class Decaf(Beverage):
    def __init__(self):
        self.description = 'Decaf and sleep better'

    def cost(self):
        return .5

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self):
        return self.beverage.description + ', Mocha'
    
    def cost(self):
        return fsum([self.beverage.cost(), .2])


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self):
        return self.beverage.description + ', Milk'
    
    def cost(self):
        return fsum([self.beverage.cost(), .1])
    

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self):
        return self.beverage.description + ', Whip'
    
    def cost(self):
        return fsum([self.beverage.cost(), .10])
    

class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self):
        return self.beverage.description + ', Soy'
    
    def cost(self):
        return fsum([self.beverage.cost(), .15])
    

class ColdBrew(Beverage):
    def __init__(self):
        self.description = '콜드브루'

    def cost(self):
        return 2.99

def starbuzz_coffee(argv = None):
    beverage: Beverage = Espresso()
    print(beverage.description)

    beverage_2: Beverage = GuatemalaAntigua()
    print(beverage_2.description)

    beverage_2 = Mocha(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Soy(beverage_2)
    print(beverage_2.description, beverage_2.cost())

    beverage_3: Beverage = ColdBrew()
    beverage_3 = Soy(beverage_3)
    beverage_3 = Soy(beverage_3)
    beverage_3 = Soy(beverage_3)
    print(beverage_3.description, beverage_3.cost())



if __name__ == '__main__': 
    starbuzz_coffee()
    
