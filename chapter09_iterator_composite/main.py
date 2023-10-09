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


class MockArray(list):
    def __init__(self, max_items: int):
        super().__init__()
        self.MAX_ITEMS = max_items

    def append(self, item):
        if len(self) < self.MAX_ITEMS:
            super().append(item)
        else:
            raise Exception("Capacity exceded. Can't add more item.")


class DinerMenu:
    def __init__(self):
        self.menu_items = MockArray(6)
    
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
        self.menu_items.append(menu_item)
    

if __name__ == '__main__':
    p = PancakeHouseMenu()
    print(p.menu_items)

    d = DinerMenu()
    print(d.menu_items)
