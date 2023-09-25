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

    def set_commands(self, slot: int, on_command: Command, off_command: Command):
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
    # light = Light()
    # light_on = LightOnCommand(light)

    # door = GarageDoor()
    # garage_open = GarageDoorOpenCommand(door)

    # rc = SimpleRemoteControl()
    # rc.slot = light_on
    # rc.button_was_pressed()

    # rc.slot = garage_open   # 종업원?
    # rc.button_was_pressed()

    remote_control = RemoteControl()

    living_room_light = Light('Living Room')
    kitchen_light = Light('Kitchen Light')
    garage_door = GarageDoor('Garage Door')
    stereo = Stereo('Living Room')

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    garage_door_up = GarageDoorOpenCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_CD = StereoOnWithCDCommand(stereo)
    stereo_off_with_CD = StereoOffWithCDCommand(stereo)

    remote_control.set_commands(0, living_room_light_on, living_room_light_off)
    remote_control.set_commands(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_commands(2, stereo_on_with_CD, stereo_off_with_CD)
    remote_control.set_commands(3, garage_door_up, garage_door_down)

    print(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)
