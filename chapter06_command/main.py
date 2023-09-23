from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    '''<< interface >>'''
    @abstractmethod
    def execute(self) -> None:
        pass


class Light:
    def on(self):
        print('light is on')


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class GarageDoor:
    def up(self):
        print('door is upping')
    
    def down(self):
        print('door is downing')

    def stop(self):
        print('door has stopped')
    
    def light_on(self):
        print('light on')
    
    def light_off(self):
        print('light off')


class GarageDoorOpenCommand(Command):
    def __init__(self, door):
        self.door = door

    def execute(self) -> None:
        self.door.up()


class SimpleRemoteControl:
    def __init__(self):
        self.slot = None

    def button_was_pressed(self):
        self.slot.execute()


if __name__ == '__main__':
    light = Light()
    light_on = LightOnCommand(light)

    door = GarageDoor()
    garage_open = GarageDoorOpenCommand(door)

    rc = SimpleRemoteControl()
    rc.slot = light_on
    rc.button_was_pressed()

    rc.slot = garage_open   # 종업원?
    rc.button_was_pressed()
