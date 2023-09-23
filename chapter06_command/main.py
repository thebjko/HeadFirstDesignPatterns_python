from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    '''<< interface >>'''
    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class SimpleRemoteControl:
    def __init__(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()

if __name__ == '__main__':
    rc = SimpleRemoteControl()
    rc.button_was_pressed()