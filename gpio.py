from servo import servo1, servo2
from stepper import step_forward, step_backward
from time import sleep

# project flow:
# for every medicine:
# move x-axis stepper
# move y-axis stepper
# move front servo (tongue)
# move back y-axis stepper
# move back x-axis stepper
# move back servo

DEGREES = 180

servos = [servo1, servo2]


def get_medicine(position):
    row, col = position.values()
    print(f"row: {row}, col: {col}")

    servo1.min()
    sleep(1)

    step_forward(DEGREES * row)
    sleep(1)

    servo1.max()
    sleep(1)

    step_backward(DEGREES * row)
    sleep(1)


def servo_shelf(position, open_shelf=False):
    row, col = position.values()
    print(f"row: {row}, col: {col}")

    # use row to specify the shelf (servo)
    selected_servo = select_servo(row)

    # TODO: use col to light a LED

    if open_shelf:
        selected_servo.max()
    else:
        selected_servo.min()

    return True


def select_servo(row):
    return servos[row]
