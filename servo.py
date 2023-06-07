from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, AngularServo

# Create a PiGPIOFactory object for the local Pi
factory = PiGPIOFactory()

# Set the pin factory for gpiozero to use the PiGPIOFactory object
Device.pin_factory = factory

# TODO: specify the initial angle of the servos
eff_servo = AngularServo(25, min_angle=-90, max_angle=90)
efb_servo = AngularServo(16, min_angle=-90, max_angle=90)
shelf_servo = AngularServo(26, min_angle=-90, max_angle=90)
