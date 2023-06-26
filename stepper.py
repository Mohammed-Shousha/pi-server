from gpiozero import OutputDevice
from time import sleep

# Define GPIO pins for IN1, IN2, IN3, IN4
F_IN1 = OutputDevice(17)
F_IN2 = OutputDevice(27)
F_IN3 = OutputDevice(22)
F_IN4 = OutputDevice(18)

B_IN1 = OutputDevice(10)
B_IN2 = OutputDevice(9)
B_IN3 = OutputDevice(11)
B_IN4 = OutputDevice(8)


f_pins = [F_IN1, F_IN2, F_IN3, F_IN4]
b_pins = [B_IN1, B_IN2, B_IN3, B_IN4]


# Define sequence of control signals for stepping motor
SEQ = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]

REV_SEQ = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
]

STEPS_PER_REV = 512
ONE_REV_DEG = 360

B_ANGLE = 140  # back angle
F_ANGLE = 130  # forward angle


def step(pins, angle=ONE_REV_DEG, backward=False):
    steps = int(angle * STEPS_PER_REV / ONE_REV_DEG)

    sequence = REV_SEQ if backward else SEQ

    for _ in range(steps):
        for seq in sequence:
            for i in range(len(pins)):
                pins[i].value = seq[i]
            sleep(0.001)

    stop(pins)


def stop(pins):
    for pin in pins:
        pin.value = 0


def step_f_forward(angle):
    step(f_pins, angle)


def step_f_backward(angle):
    step(f_pins, angle, True)


def step_b_forward(angle):
    step(b_pins, angle)


def step_b_backward(angle):
    step(b_pins, angle, True)


def back_movement():
    step_b_forward(B_ANGLE)
    sleep(1)
    step_b_backward(B_ANGLE)
    sleep(1)


def front_movement():
    step_f_forward(F_ANGLE)
    sleep(1)
    step_f_backward(F_ANGLE-1)
    sleep(1)
