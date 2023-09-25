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

    def on(self, val = 11):
        print('stereo is on')
        self.set_CD()
        self.set_volume(val)

    def off(self, val = 0):
        self.set_volume(val)
        self.set_CD()
        print('stereo is off')
    
    def set_CD(self):
        print('CD is set')

    def set_volume(self, val: int):
        print(f'volume is set to {val}')
