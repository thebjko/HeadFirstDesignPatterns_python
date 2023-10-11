from abc import ABC, abstractmethod


class Iterator(ABC):
    '''<< Interface >>'''
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass
    

class DinerMenuIterator(Iterator):
    def __init__(self, items):
        if isinstance(items, dict):
            self.items = items
        else:
            raise TypeError('Items must be of type dict.')
        self.position = 0

    def next(self):
        menu_item = self.items.get(self.position)
        self.position += 1
        return menu_item

    def has_next(self):
        if self.position >= len(self.items) or self.items.get(self.position) is None:
            return False
        return True
