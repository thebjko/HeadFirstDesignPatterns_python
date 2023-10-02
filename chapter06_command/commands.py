from abc import ABCMeta, abstractmethod

from receivers import *


class Command(metaclass=ABCMeta):
    '''<< interface >>'''
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(Command):
    '''concrete command'''
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightOffCommand(Command):
    '''concrete command'''
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()


class GarageDoorOpenCommand(Command):
    '''concrete command'''
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self) -> None:
        self.door.up()

    def undo(self) -> None:
        self.door.down()

class GarageDoorDownCommand(Command):
    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.down()

    def undo(self) -> None:
        self.door.up()

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volume(11)

    def undo(self):
        self.stereo.set_volume(0)
        self.stereo.set_CD()
        self.stereo.off()


class StereoOffWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.set_volume(0)
        self.stereo.set_CD()
        self.stereo.off()
    
    def undo(self):
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volume(11)

class NoCommand:
    '''?'''
    def execute(self):
        print('no commands on this slot')

    def undo(self):
        pass


class CeilingFanCommand(Command):
    def __init__(self, ceiling_fan) -> None:
        self.ceiling_fan = ceiling_fan
    
    def execute(self) -> None:
        self.prev_speed = self.ceiling_fan.get_speed()

    def undo(self):
        match self.prev_speed:
            case CeilingFanSpeed.HIGH:
                self.ceiling_fan.high()
            case CeilingFanSpeed.MEDIUM:
                self.ceiling_fan.medium()
            case CeilingFanSpeed.LOW:
                self.ceiling_fan.low()
            case CeilingFanSpeed.OFF:
                self.ceiling_fan.off()


class CeilingFanHighCommand(CeilingFanCommand):
    def execute(self) -> None:
        super().execute()
        self.ceiling_fan.high()


class CeilingFanMediumCommand(CeilingFanCommand):
    def execute(self) -> None:
        super().execute()
        self.ceiling_fan.medium()


class CeilingFanLowCommand(CeilingFanCommand):
    def execute(self) -> None:
        super().execute()
        self.ceiling_fan.low()


class CeilingFanOffCommand(CeilingFanCommand):
    def execute(self) -> None:
        super().execute()
        self.ceiling_fan.off()


class TVOnCommand(Command):
    def __init__(self, tv) -> None:
        self.tv = tv

    def execute(self) -> None:
        self.tv.on()
    
    def undo(self):
        self.tv.off()


class TVOffCommand(Command):
    def __init__(self, tv) -> None:
        self.tv = tv

    def execute(self) -> None:
        self.tv.off()
    
    def undo(self):
        self.tv.on()


class HottubOnCommand(Command):
    def __init__(self, hottub) -> None:
        self.hottub = hottub

    def execute(self) -> None:
        self.hottub.on()

    def undo(self):
        self.hottub.off()


class HottubOffCommand(Command):
    def __init__(self, hottub) -> None:
        self.hottub = hottub

    def execute(self) -> None:
        self.hottub.off()

    def undo(self):
        self.hottub.on()


class MacroCommand(Command):
    def __init__(self, commands: list[Command]):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()

