from gpiozero import DigitalOutputDevice
from time import sleep
from enum import Enum

STEPS_PER_REV = 200  # at 1:1 microstepping

# Define the pins for the TB6600 driver
PUL_X = DigitalOutputDevice(20)
DIR_X = DigitalOutputDevice(21)

PUL_Y = DigitalOutputDevice(23)
DIR_Y = DigitalOutputDevice(24)

class Direction(Enum):
    CW = True
    CCW = False


class Axis(Enum):
    X = "x"
    Y = "y"


steppers = {
    Axis.X: {"DIR": DIR_X, "PUL": PUL_X},
    Axis.Y: {"DIR": DIR_Y, "PUL": PUL_Y},
}

def stepper(axis=Axis.X, steps=STEPS_PER_REV, direction=Direction.CW, delay=0.001):

    DIR, PUL = steppers[axis].values()

    print('dir: ', DIR, 'pul: ', PUL, 'steps: ', steps,
          'direction: ', direction, 'delay: ', delay, '\n')

    if direction == Direction.CW:
        DIR.on()
    else:
        DIR.off()

    for _ in range(steps):
        PUL.on()
        sleep(delay)
        PUL.off()
        sleep(delay)


def stepper_x_cw(steps):
    stepper(Axis.X, steps, Direction.CW)

def stepper_x_ccw(steps):
    stepper(Axis.X, steps, Direction.CCW)

def stepper_y_cw(steps):
    stepper(Axis.Y, steps, Direction.CW)

def stepper_y_ccw(steps):
    stepper(Axis.Y, steps, Direction.CCW)


# def axis_movement(x_steps = 200, y_steps=200):
#     stepper_x_cw(x_steps)
#     sleep(1)
#     stepper_y_cw(y_steps)
#     sleep(1)
#     stepper_x_ccw(x_steps)
#     sleep(1)
#     stepper_y_ccw(y_steps)