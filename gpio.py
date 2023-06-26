from nema_stepper import stepper_x_cw, stepper_x_ccw, stepper_y_cw, stepper_y_ccw
from stepper import front_movement, back_movement
from relay import shelves
from time import sleep

# project flow:
# for every medicine:
# move x-axis stepper
# move y-axis stepper
# move front end-effector
# move back y-axis stepper
# move back x-axis stepper
# move back end-effector

X_STEPS = 180
Y_STEPS = 180


def get_medicine(position, quantity):

    row, col = position.values()

    stepper_x_cw(X_STEPS * row)
    sleep(1)

    stepper_y_cw(Y_STEPS * col)
    sleep(1)

    for _ in range(quantity):
        front_movement()

    stepper_y_ccw(Y_STEPS * col)
    sleep(1)

    stepper_x_ccw(X_STEPS * row)
    sleep(1)

    back_movement()

    return True


# use row to specify the shelf
# use col to light a LED (or something) to indicate the medicine

def open_shelf(row, col):

    shelves[row].on()

    return True


def close_shelf(row, col):

    shelves[row].off()

    return True
