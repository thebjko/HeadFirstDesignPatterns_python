from iterators import DinerMenuIterator, PythonicIterator


class MenuItem:
    def __init__(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float
    ):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def __repr__(self):
        return self.name


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items = []

        self.add_item(
            'K&B Pancake Set',
            'Pancake with scrambled egg and toast',
            True,
            2.99
        )

        self.add_item(
            'Regular Pancake Set',
            'Pancake with egg fry and sausage',
            False,
            2.99
        )
    
        self.add_item(
            'Blueberry Pancake',
            'Pancake made with fresh blueberry and blueberry syrup',
            True,
            3.49
        )
    
        self.add_item(
            'Waffle',
            'Waffle where you can add blueberry or strawberry accoring to your preference',
            True,
            3.59
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)


class DinerMenu:
    def __init__(self):
        self.menu_items = {}
    
        self.add_item(
            'Vegetarian BLT',
            'Whole wheat, Bean Meat Bacon, Lettuce, Tomato',
            True,
            2.99    
        )
    
        self.add_item(
            'BLT',
            'Whole wheat, Bacon, Lettuce, Tomato',
            False,
            2.99
        )
            
        self.add_item(
            'Today\'s Soup',
            'Today\'s Soup with Potato Salad',
            False,
            3.29
        )
    
        self.add_item(
            'Hot Dog',
            'Sourcraut, Spices, Onion, Cheese',
            False,
            3.05    
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.update({len(self.menu_items): menu_item})
    
    def create_iterator(self):
        return PythonicIterator(self.menu_items)


if __name__ == '__main__':
    pancakehouse_menu = PancakeHouseMenu()
    breakfast_items = pancakehouse_menu.menu_items

    diner_menu = DinerMenu()
    lunch_items = diner_menu.menu_items