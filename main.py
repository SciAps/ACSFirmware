from Motors import RotationMotor, LinearMotor

rotationMotor = RotationMotor()
linearMotor = LinearMotor()
while True:
    a = input()
    try:
        if a == 'U':
            linearMotor.raisePlatform()
        elif a == 'D':
            linearMotor.lowerPlatform()
        elif a == 'H':
            rotationMotor.home()
        elif a == 'N':
            rotationMotor.moveOneSampleForward()
        elif a == 'B':
            rotationMotor.moveOneSampleBackwards()
        elif a.isdigit():
            rotationMotor.rotateMotor(int(a))
        elif a == 'P':
            rotationMotor.getPos()
        elif a == 'ping':
            print('pong')
        else:
            print('commandNotFound_ascr')
    except:
        print('exception_acsr')
    