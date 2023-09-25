from abc import ABCMeta, abstractmethod

from receivers import *


class Command(metaclass=ABCMeta):
    '''<< interface >>'''
    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    '''concrete command'''
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class GarageDoorOpenCommand(Command):
    '''concrete command'''
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self) -> None:
        self.door.up()
