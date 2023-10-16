class Waitress:
    def __init__(self, pancakehouse_menu, diner_menu):
        self.pancakehouse_menu = pancakehouse_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        pancake_iterator = self.pancakehouse_menu.create_iterator()
        diner_iterator = self.diner_menu.create_iterator()

        print('메뉴\n---\n아침 메뉴')
        self._print_menu(pancake_iterator)
        print('\n점심 메뉴')
        self._print_menu(diner_iterator)

    def _print_menu(self, iterator):
        for menu_item in iterator:
            print(f'{menu_item.name}, {menu_item.price} -- {menu_item.description}')
            
        # while iterator.has_next():
        #     menu_item = next(iterator)
        #     print(f'{menu_item.name}, {menu_item.price} -- {menu_item.description}')
