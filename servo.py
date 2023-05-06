from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo, Device, AngularServo
from time import sleep

# Create a PiGPIOFactory object for the local Pi
factory = PiGPIOFactory()

# Set the pin factory for gpiozero to use the PiGPIOFactory object
Device.pin_factory = factory

servo = AngularServo(23, min_angle=-90, max_angle=90)

def min_servo():
    servo.min()

def max_servo():
    servo.max()

def mid_servo():
    servo.mid()

def servo_angle(angle):
    servo.angle = angle