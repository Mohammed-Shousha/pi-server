from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, AngularServo

# Create a PiGPIOFactory object for the local Pi
factory = PiGPIOFactory()

# Set the pin factory for gpiozero to use the PiGPIOFactory object
Device.pin_factory = factory

# TODO: specify the initial angle of the servo
servo1 = AngularServo(23, min_angle=-90, max_angle=90)
servo2 = AngularServo(4, min_angle=-90, max_angle=90)


def min_servo():
    servo1.min()


def max_servo():
    servo1.max()


def mid_servo():
    servo1.mid()


def servo_angle(angle):
    servo1.angle = angle
