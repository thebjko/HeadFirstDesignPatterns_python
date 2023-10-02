from enums import *


class CeilingFan:
    def __init__(self, location: str):
        self.location = location
        self.speed = CeilingFanSpeed.OFF

    def high(self):
        self.speed = CeilingFanSpeed.HIGH

    def medium(self):
        self.speed = CeilingFanSpeed.MEDIUM

    def low(self):
        self.speed = CeilingFanSpeed.LOW

    def off(self):
        self.speed = CeilingFanSpeed.OFF

    def get_speed(self):
        return self.speed


class Light:
    def __init__(self, desc: str):
        self.description = desc

    def on(self):
        print('light is on')

    def off(self):
        print('light is off')


class GarageDoor:
    def __init__(self, desc: str):
        self.description = desc
        
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


class Stereo:
    def __init__(self, desc: str):
        self.description = desc

    def on(self):
        print('stereo is on')

    def off(self):
        print('stereo is off')
    
    def set_CD(self):
        print('CD is set')

    def set_volume(self, val: int):
        print(f'volume is set to {val}')
