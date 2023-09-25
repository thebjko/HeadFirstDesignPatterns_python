class Light:
    def on(self):
        print('light is on')

    def off(self):
        print('light is off')


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


class Stereo:
    def on(self):
        print('stereo is on')
    
    def set_CD(self):
        print('CD is set')

    def set_volume(val: int):
        print(f'volume is set to {val}')
