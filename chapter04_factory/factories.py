from abc import ABC, abstractmethod

from ingredients import *


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
    