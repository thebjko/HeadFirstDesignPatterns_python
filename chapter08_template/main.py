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


class CoffeeWithHook(CaffeineBeverage):

    def brew(self):
        print('brewing coffee')

    def add_condiments(self):
        print('adding sugar and milk')

    def customer_wants_condiments(self):
        answer = input('커피에 우유와 설탕을 넣을까요? [y/n] ')

        if answer.startswith('y'):
            return True
        return False


class TeaWithHook(CaffeineBeverage):

    def brew(self):
        print('brewing tea')

    def add_condiments(self):
        print('adding lemon')

    def customer_wants_condiments(self):
        answer = input('홍차에 레몬을 넣을까요? [y/n] ')

        if answer.startswith('y'):
            return True
        return False


if __name__ == '__main__':
    c = CoffeeWithHook()
    c.prepare_recipe()

    t = TeaWithHook()
    t.prepare_recipe()
