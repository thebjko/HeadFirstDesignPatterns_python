from abc import ABC, abstractmethod

from pizzas import *


class PizzaStore(ABC):

    @abstractmethod
    def _create_pizza(self, pizza_type: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        self.pizza: Pizza = self._create_pizza(pizza_type)

        if self.pizza is not None:

            self.pizza.prepare()
            self.pizza.bake()
            self.pizza.cut()
            self.pizza.box()

            return self.pizza


class NYPizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case 'cheese':
                return NYStyleCheesePizza()
            case 'pepperoni':
                return NYStylePepperoniPizza()
            case 'clam':
                return NYStyleClamPizza()
            case 'veggie':
                return NYStyleVeggiePizza()


class ChicagoPizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case 'cheese':
                return ChicagoCheesePizza()
            case 'pepperoni':
                return ChicagoPepperoniPizza()
            case 'clam':
                return ChicagoClamPizza()
            case 'veggie':
                return ChicagoVeggiePizza()


class CaliforniaPizzaStore(PizzaStore):

    def _create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case 'cheese':
                return CaliforniaCheesePizza()
            case 'pepperoni':
                return CaliforniaPepperoniPizza()
            case 'clam':
                return CaliforniaClamPizza()
            case 'veggie':
                return CaliforniaVeggiePizza()


if __name__ == '__main__':
    store = ChicagoPizzaStore()
    print(store.order_pizza('cheesde'))
