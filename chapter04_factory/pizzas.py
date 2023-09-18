from abc import ABC, abstractmethod


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: list[str] = []
    
    def prepare(self):
        print('준비 중:', self.name)
        print('도우를 돌리는 중...')
        print('소스를 뿌리는 중...')
        print('토핑을 올리는 중: ')
        for t in self.toppings:
            print(' ' + t)

    def bake(self):
        print('175도에서 25분 간 굽기')

    def cut(self):
        print('피자를 사선으로 자르기')

    def box(self):
        print('상자에 피자 담기')


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = '뉴욕 스타일 소스와 치즈 피자'
        self.dough = '씬 크러스트 도우'
        self.sauce = '마리나라 소스'

        self.toppings.append('잘게 썬 레지아노 치즈')


class NYStylePepperoniPizza(Pizza):
    pass


class NYStyleVeggiePizza(Pizza):
    pass


class NYStyleClamPizza(Pizza):
    pass


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        self.name = '시카고 스타일 딥 디쉬 치즈 피자'
        self.dough = '아주 두꺼운 크러스트 도우'
        self.sauce = '플럼토마토 소스'

        self.toppings.append('잘게 조각낸 모짜렐라 치즈')

    def cut(self):
        print('네모난 모양으로 피자 자르기')


class ChicagoPepperoniPizza(Pizza):
    pass


class ChicagoVeggiePizza(Pizza):
    pass


class ChicagoClamPizza(Pizza):
    pass


class CaliforniaCheesePizza(Pizza):
    pass


class CaliforniaPepperoniPizza(Pizza):
    pass


class CaliforniaVeggiePizza(Pizza):
    pass


class CaliforniaClamPizza(Pizza):
    pass
