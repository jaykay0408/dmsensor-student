#!/usr/bin/python

from Raspi_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

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
    # print(angle, analog_value)
    return analog_value


pwm.setPWMFreq(FREQUENCY)  # Set frequency to 60 Hz

while (True):
    # Change speed of continuous servo on channel O
    pwm.setPWM(1, 0, pulseWidth(0))
    time.sleep(1)
    pwm.setPWM(1, 0, pulseWidth(45))
    time.sleep(1)
    pwm.setPWM(1, 0, pulseWidth(90))
    time.sleep(1)
