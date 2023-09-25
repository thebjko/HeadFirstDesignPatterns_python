from commands import *


class SimpleRemoteControl:
    '''invoker?'''
    def __init__(self):
        self.slot = None

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    def __init__(self):
        self.on_commands = []
        self.off_commands = []

        self.no_command = NoCommand()
        for _ in range(7):
            self.on_commands.append(self.no_command)
            self.off_commands.append(self.no_command)

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()

    def __str__(self):
        print('---------- 리모컨 ----------')
        for i in range(len(self.on_commands)):
            ls = [
                f'[slot {i}]',
                self.on_commands[i].__class__.__name__,
                '    ',
                self.off_commands[i].__class__.__name__,
            ]
            print(''.join(ls))
    

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
