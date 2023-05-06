from gpiozero import OutputDevice
from time import sleep

# Define GPIO pins for IN1, IN2, IN3, IN4
IN1 = OutputDevice(17)
IN2 = OutputDevice(27)
IN3 = OutputDevice(22)
IN4 = OutputDevice(18)

pins = [IN1, IN2, IN3, IN4]

# Define sequence of control signals for stepping motor
seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]

STEPS_PER_REV = 512
ONE_REV_DEG = 360


def stop():
    IN1.value = 0
    IN2.value = 0
    IN3.value = 0
    IN4.value = 0


# Define function to step motor forward or backward
def step(angle=ONE_REV_DEG, backward=False):
    steps = int(angle * STEPS_PER_REV / ONE_REV_DEG)

    if backward == True:
        seq.reverse()

    for _ in range(steps):
        for step in seq:
            for i in range(len(pins)):
                pins[i].value = step[i]
            sleep(0.001)
    stop()


def step_forward(steps):
    step(steps)


def step_backward(steps):
    step(steps, True)
