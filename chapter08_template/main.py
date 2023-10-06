from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):
    @abstractmethod
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print('boiling water')

    def pour_in_cup(self):
        print('pouring beverage')
        


class Coffee(CaffeineBeverage):
    def prepare_recipe(self):
        super().prepare_recipe()

    def brew_coffee_grinds(self):
        pass

    def add_sugar_and_milk(self):
        pass


class Tea(CaffeineBeverage):
    def prepare_recipe(self):
        super().prepare_recipe()
    
    def steep_tea_bag(self):
        pass

    def add_lemon(self):
        pass

    
if __name__ == '__main__':
    c = Coffee()
    c.boil_water()
    c.prepare_recipe()

