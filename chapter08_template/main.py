from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print('boiling water')

    def pour_in_cup(self):
        print('pouring beverage')



class Coffee(CaffeineBeverage):

    def brew(self):
        print('brewing coffee')

    def add_condiments(self):
        print('adding sugar and milk')


class Tea(CaffeineBeverage):

    def brew(self):
        print('brewing tea')

    def add_condiments(self):
        print('adding lemon')


if __name__ == '__main__':
    c = Coffee()
    c.prepare_recipe()

    t = Tea()
    t.prepare_recipe()
