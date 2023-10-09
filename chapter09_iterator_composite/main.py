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


if __name__ == '__main__':
    p = PancakeHouseMenu()
    print(p.menu_items)
