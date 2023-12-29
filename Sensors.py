import digitalio
import microcontroller


class hall_Effect:
    def __init__(self,name, num):
        self.num= num
        self.name = name
        
        self.pin = digitalio.DigitalInOut(getattr(microcontroller.pin, dir(microcontroller.pin)[num]))
        self.pin.direction = digitalio.Direction.INPUT
    def getInput(self):
        return self.pin.value
        
    
    
class beam_Sensor_Thing:

    def __init__(self,name, num):
        self.num= num
        self.name = name

        self.pin = digitalio.DigitalInOut(getattr(microcontroller.pin, dir(microcontroller.pin)[num]))
        self.pin.direction = digitalio.Direction.INPUT

        
    def getInput(self):
        return self.pin.value
    
