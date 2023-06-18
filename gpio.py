from servo import eff_servo, efb_servo, shelf_servo
from nema_stepper import stepper_x_cw, stepper_x_ccw, stepper_y_cw, stepper_y_ccw
from time import sleep

# project flow:
# for every medicine:
# move x-axis stepper
# move y-axis stepper
# move front servo (tongue)
# move back y-axis stepper
# move back x-axis stepper
# move back servo

X_STEPS = 180
Y_STEPS = 180

def get_medicine(position, quantity):
    row, col = position.values()
    print(f"row: {row}, col: {col}, qty: {quantity}")

    stepper_x_cw(X_STEPS * row)
    sleep(1)

    stepper_y_cw(Y_STEPS * col)
    sleep(1)

    for _ in range(quantity):
        eff_servo.min()
        sleep(1)

        eff_servo.max()
        sleep(1)
    
    stepper_y_ccw(Y_STEPS * col)
    sleep(1)

    stepper_x_ccw(X_STEPS * row)
    sleep(1)

    # open the other servo to drop medicines
    efb_servo.min()
    sleep(1)
    efb_servo.max()
    sleep(1)

    return True


def shelf(position, open_shelf=False):
    row, col = position.values()
    print(f"row: {row}, col: {col}")

    # use row to specify the shelf (servo)
    # use col to light a LED

    if open_shelf:
        shelf_servo.max()
    else:
        shelf_servo.min()

    return True
