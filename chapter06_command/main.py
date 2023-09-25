from commands import *


class SimpleRemoteControl:
    '''invoker?'''
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
