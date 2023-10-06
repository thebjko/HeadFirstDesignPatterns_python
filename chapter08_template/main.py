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
    # def prepare_recipe(self):
    #     super().prepare_recipe()

    def brew(self):
        print('brewing coffee')
        # self.brew_coffee_grinds()

    def add_condiments(self):
        print('adding sugar and milk')
        # self.add_sugar_and_milk()

    def brew_coffee_grinds(self):
        print('brewing coffee')

    def add_sugar_and_milk(self):
        print('adding sugar and milk')


class Tea(CaffeineBeverage):
    # def prepare_recipe(self):
    #     super().prepare_recipe()

    def brew(self):
        print('brewing tea')
        # self.steep_tea_bag()

    def add_condiments(self):
        print('adding lemon')
        # self.add_lemon()
    
    def steep_tea_bag(self):
        print('brewing tea')

    def add_lemon(self):
        print('adding lemon')
    

if __name__ == '__main__':
    c = Coffee()
    c.prepare_recipe()

    t = Tea()
    t.prepare_recipe()
