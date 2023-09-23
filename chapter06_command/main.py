from abc import ABCMeta, abstractmethod


class Command(metaclas=ABCMeta):
    '''<< interface >>'''
    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        self.light.on()
