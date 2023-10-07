from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
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

    def customer_wants_condiments(self):
        '''hook'''
        return True


class Coffee(CaffeineBeverage):
    def __init__(self, condiment=True) -> None:
        self.condiments_flag = condiment

    def brew(self):
        print('brewing coffee')

    def add_condiments(self):
        print('adding sugar and milk')

    def customer_wants_condiments(self):
        return self.condiments_flag


class Tea(CaffeineBeverage):

    def brew(self):
        print('brewing tea')

    def add_condiments(self):
        print('adding lemon')


if __name__ == '__main__':
    c = Coffee(condiment=False)
    c.prepare_recipe()

    t = Tea()
    t.prepare_recipe()
