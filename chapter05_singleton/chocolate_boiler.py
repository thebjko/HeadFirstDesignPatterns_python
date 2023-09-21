'''https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/'''


class ChocolateBoiler:
    __empty: bool
    __boild: bool

    def __init__(self):
        print(self)
        super().__init__()

    # def __new__(cls):
    #     print('new called')    
    #     return super().__new__(cls)
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('no instance')
            cls.instance = super().__new__(cls)
        else:
            print('instance already exists.')
        return cls.instance
        
    @classmethod
    def is_empty(cls):
        return cls.__empty

    @classmethod
    def fill(cls, val: bool):
        cls.__empty = val


if __name__ == '__main__':
    cb = ChocolateBoiler()
    # cb2 = cb.__new__(cb.__class__)
    cb2 = ChocolateBoiler()