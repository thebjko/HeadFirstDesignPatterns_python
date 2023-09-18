from pizzas import *

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
