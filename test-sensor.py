'''
**********************************************************************
* Filename    : test-sensor.py
* Description : test control for servo and DC motors
* Update      : Lee    2021-08-20    New release
**********************************************************************
'''
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F)

servoMin = 600  # Min pulse length out of 4096 (150)
servoMax = 2650  # Max pulse length out of 4096 (600)
FREQUENCY = 60


#  Prominent Arduino map function
def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


# Angle to Pulse Width
def pulseWidth(angle):
    pulse_wide = map(angle, 0, 180, servoMin, servoMax)
    analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096)
    return analog_value


SPEED = 0
myMotor = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(SPEED)
myMotor.run(Raspi_MotorHAT.FORWARD)
# turn on motor
myMotor.run(Raspi_MotorHAT.RELEASE)

while True:
    key = input("> ")
    SPEED = 50

    if key == 'q':
        break
    elif key == 'w':
        myMotor.setSpeed(SPEED)
        myMotor.run(Raspi_MotorHAT.FORWARD)
    elif key == 'x':
        myMotor.setSpeed(SPEED)
        myMotor.run(Raspi_MotorHAT.BACKWARD)
    elif key == 'a':
        pwm.setPWM(1, 0, pulseWidth(45))
    elif key == 'd':
        pwm.setPWM(1, 0, pulseWidth(135))
    elif key == 's':
        pwm.setPWM(1, 0, pulseWidth(90))
    elif key == 'z':
        SPEED = 0
