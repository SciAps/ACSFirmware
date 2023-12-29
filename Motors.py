from Sensors import hall_Effect, beam_Sensor_Thing
import time
import board
import digitalio

step = digitalio.DigitalInOut(board.GP16)
step.direction = digitalio.Direction.OUTPUT

mdir = digitalio.DigitalInOut(board.GP17)
mdir.direction = digitalio.Direction.OUTPUT

en = digitalio.DigitalInOut(board.GP18)
en.direction = digitalio.Direction.OUTPUT

fan = digitalio.DigitalInOut(board.GP4)
fan.direction = digitalio.Direction.OUTPUT

a = beam_Sensor_Thing('a', 7)
b = beam_Sensor_Thing('b', 6)
c = hall_Effect('c', 26)


class LinearMotor:
    en.value = True
    fan.value = True

    def __init__(self):
        self.platform_raised = False

    def lowerPlatform(self):
        en.value = False
        fan.value = True
        while a.getInput() == False:
            step.value = True
            time.sleep(0.001)
            step.value = False
            time.sleep(0.001)
        print('dn')
        self.platform_raised = False
        fan.value = False
        en.value = True

    def raisePlatform(self):
        en.value = False
        fan.value = True
        #todo self.platform_raised can be removed when a raised sensor is added
        if self.platform_raised == False:
            for i in range(1760):
                step.value = True
                time.sleep(0.001)
                step.value = False
                time.sleep(0.001)
        print('up')
        self.platform_raised = True
        en.value = True
        fan.value = False


m2step = digitalio.DigitalInOut(board.GP19)
m2step.direction = digitalio.Direction.OUTPUT

m2dir = digitalio.DigitalInOut(board.GP20)
m2dir.direction = digitalio.Direction.OUTPUT

m2en = digitalio.DigitalInOut(board.GP21)
m2en.direction = digitalio.Direction.OUTPUT


class RotationMotor:
    m2en.value = True
    m2dir.value = False

    def __init__(self):
        self.homed = False
        self.current_pos = 0

    def home(self):
        m2en.value = False
        lastPingTime = 0
        if self.homed == False:
            while b.getInput() == False:
                m2step.value = True
                time.sleep(0.001)
                m2step.value = False
                time.sleep(0.001)

                if time.time() - lastPingTime >= 3:
                    lastPingTime = time.time()
                    print("homing")

            self.homed = True
            self.current_pos = 0
        print('home')
        m2en.value = True


    def moveOffSample(self):
        while c.getInput() == True:
            m2step.value = True
            time.sleep(0.001)
            m2step.value = False
            time.sleep(0.001)

    def moveToSample(self):
        while c.getInput() == False:
            m2step.value = True
            time.sleep(0.001)
            m2step.value = False
            time.sleep(0.001)

        if b.getInput() == True:
            self.homed = True
            self.current_pos = 0
        else:
            if m2dir.value == False:
                self.current_pos += 1
            else:
                self.current_pos -= 1



    def rotateMotor(self, sample = 0):
        m2en.value = False
        m2dir.value = sample < self.current_pos
        lastPingTime = 0
        numSamplesToMove = abs(sample - self.current_pos)
        for i in range(numSamplesToMove):
            self.moveOffSample()
            self.moveToSample()
            if time.time() - lastPingTime >= 3:
                lastPingTime = time.time()
                print('Pos ' + str(self.current_pos))

        print('R' + str(self.current_pos))

        m2en.value = True

    def moveOneSampleForward(self):
        newSample = self.current_pos + 1
        self.rotateMotor(newSample)

    def moveOneSampleBackwards(self):
        newSample = self.current_pos - 1
        self.rotateMotor(newSample)

    def getPos(self):
        print(str(self.current_pos))
