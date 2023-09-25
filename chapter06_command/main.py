from receivers import *


class SimpleRemoteControl:
    '''invoker?'''
    def __init__(self):
        self.slot = None

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    def __init__(self):
        self.on_commands = [None] * 7
        self.off_commands = [None] * 7

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot]()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot]()

    def set_commands(self, slot: int, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def __str__(self):
        print('---------- 리모컨 ----------')
        ls = []
        for i in range(len(self.on_commands)):
            x = [
                f'[slot {i}]',
                self.on_commands[i].__class__.__name__,
                '    ',
                self.off_commands[i].__class__.__name__,
            ]
            ls.append(''.join(x))
        return '\n'.join(ls)
    

if __name__ == '__main__':

    remote_control = RemoteControl()

    living_room_light = Light('Living Room')
    kitchen_light = Light('Kitchen Light')
    garage_door = GarageDoor('Garage Door')
    stereo = Stereo('Living Room')

    remote_control.set_commands(0, lambda: living_room_light.on(), lambda: living_room_light.off())
    remote_control.set_commands(1, lambda: kitchen_light.on(), lambda: kitchen_light.off())
    remote_control.set_commands(2, lambda: stereo.on(11), lambda: stereo.off(0))
    remote_control.set_commands(3, lambda: garage_door.up(), lambda: garage_door.down())

    print(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)
