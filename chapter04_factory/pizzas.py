from abc import ABC, abstractmethod

from ingredient_factories import *


class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    veggies: list[Veggies]
    cheese: Cheese
    pepperoni: Pepperoni
    clam: Clam

    @abstractmethod
    def prepare(self):
        '''
        원재료 팩토리에서 재료들을 가져오는 메서드
        '''
        pass

    def bake(self):
        print('175도에서 25분 간 굽기')

    def cut(self):
        print('피자를 사선으로 자르기')

    def box(self):
        print('상자에 피자 담기')

    def __str__(self):
        return self.name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory   # 객체 구성

    def prepare(self):
        print('준비중:', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('준비중:', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('준비중:', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = '뉴욕 스타일 소스와 치즈 피자'
        self.dough = '씬 크러스트 도우'
        self.sauce = '마리나라 소스'

        self.toppings.append('잘게 썬 레지아노 치즈')


class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('준비중:', self.name)
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        veggies = self.ingredient_factory.create_veggies()

class NYStylePepperoniPizza(Pizza):
    pass


class NYStyleVeggiePizza(Pizza):
    pass


class NYStyleClamPizza(Pizza):
    pass


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        self.name = '시카고 스타일 딥 디쉬 치즈 피자'
        self.dough = '아주 두꺼운 크러스트 도우'
        self.sauce = '플럼토마토 소스'

        self.toppings.append('잘게 조각낸 모짜렐라 치즈')

    def cut(self):
        print('네모난 모양으로 피자 자르기')


class ChicagoPepperoniPizza(Pizza):
    pass


class ChicagoVeggiePizza(Pizza):
    pass


class ChicagoClamPizza(Pizza):
    pass


class CaliforniaCheesePizza(Pizza):
    pass


class CaliforniaPepperoniPizza(Pizza):
    pass


class CaliforniaVeggiePizza(Pizza):
    pass


class CaliforniaClamPizza(Pizza):
    pass
