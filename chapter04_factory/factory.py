from abc import ABC, abstractmethod
from chapter04_factory.ingredients import Cheese, Clam, Dough, Pepperoni, Sauce, Veggies

from pizzas import *
from ingredients import *

class SimplePizzaFactory:
    def __init__(self, pizza_type: str):
        self.pizza_type = pizza_type
    
    def create_pizza(self, pizza_type: str) -> Pizza:
        self.pizza: Pizza = None

        if pizza_type == 'Cheese':
            pizza = CheesePizza()
        elif pizza_type == 'Pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'Veggie':
            pizza = VeggiePizza()

        return self.pizza


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> list[Veggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> Clam:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_cheese(self) -> Cheese:
        return ReggianoCheese()
    
    def create_sauce(self) -> Sauce:
        return MarinaraSauce()
    
    def create_veggies(self) -> list[Veggies]:
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    
    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
    
    def create_clam(self) -> Clam:
        return FreshClam()
    
    def create_dough(self) -> Dough:
        return ThinCrustDough
    

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()
    
    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()
    
    def create_veggies(self) -> list[Veggies]:
        veggies = [EggPlant(), Spinach(), BlackOlives()]
        return veggies
    
    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
    
    def create_clam(self) -> Clam:
        return FrozenClam()
    
    def create_dough(self) -> Dough:
        return ThickCrustDough
    