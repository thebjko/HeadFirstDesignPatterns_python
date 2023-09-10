from abc import ABC, abstractmethod


# interface equivalence
class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        pass


# abstract class
class Character(ABC):
    def __init__(self, weapon_behavior: WeaponBehavior):
        self.weapon_behavior = weapon_behavior
    
    def set_weapon(self, weapon_behavior: WeaponBehavior):
        self.weapon = weapon_behavior

    # @abstractmethod
    def fight(self):
        self.weapon_behavior.use_weapon()


class King(Character):
    # def __init__(self, weapon_behavior: WeaponBehavior):
    #     super().__init__(weapon_behavior)
    
    # def fight(self):
    #     self.weapon_behavior.use_weapon()
    pass

class Queen(Character):
    # def fight(self):
    #     pass
    pass
class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print('대략 칼을 사용')


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('대략 도끼를 사용')


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print('대략 활과 화살을 사용')


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('대략 나이프를 사용')

    
if __name__ == '__main__':
    sword_behavior = SwordBehavior()
    king = King(sword_behavior)
    king.fight()

    queen = Queen(BowAndArrowBehavior())
    queen.fight()