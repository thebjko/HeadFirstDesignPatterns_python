from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def milk(self):
        pass

    @milk.setter
    @abstractmethod
    def milk(self, val):
        pass

    # @property
    # @abstractmethod
    # def whip(self):
    #     pass

    # @whip.setter
    # @abstractmethod
    # def whip(self):
    #     pass

class ColdBrew(Beverage):
    def __init__(self):
        self.__description = False
        self.__milk = False
        self.__soy = False
        self.__mocha = False
        self.__whip = False

    def cost(self):
        pass

    @property
    def milk(self):
        return self.__milk
    
    @milk.setter
    def milk(self, val):
        self.__milk = val
    
    

if __name__ == '__main__':
    cold_brew = ColdBrew()
    print(cold_brew.milk)
    cold_brew.milk = 12
    print(cold_brew.milk)
    
