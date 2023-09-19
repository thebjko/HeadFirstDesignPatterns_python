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
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()

        match pizza_type:
            case 'cheese':
                pizza = CheesePizza(ingredient_factory)
                pizza.name = '뉴욕 스타일 치즈 피자'
            case 'pepperoni':
                pizza = PepperoniPizza(ingredient_factory)
                pizza.name = '뉴욕 스타일 페퍼로니 피자'
            case 'clam':
                pizza = ClamPizza(ingredient_factory)
                pizza.name = '뉴욕 스타일 클램 피자'
            case 'veggie':
                pizza = VeggiePizza(ingredient_factory)
                pizza.name = '뉴욕 스타일 야채피자'
            case _ :
                return
        
        return pizza


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
