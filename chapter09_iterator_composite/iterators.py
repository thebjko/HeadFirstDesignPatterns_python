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


class PythonicIterator:
    def __init__(self, items):
        self.items = items
        self.position = 0
        self.sentinel = object()

    def __iter__(self):
        return self

    def __next__(self):
        if self.items and self.position < len(self.items):
            item = self.items[self.position]
            self.position += 1
            return item
        raise StopIteration

    def has_next(self):
        n = next(self, self.sentinel)
        if n is self.sentinel:
            return False
        self.position -= 1
        return True


if __name__ == '__main__':
    it = PythonicIterator([1,2,3])
    print(next(it))
    print(it.has_next())
    print(next(it))
    print(it.has_next())
    print(next(it))
    print(it.has_next())
    