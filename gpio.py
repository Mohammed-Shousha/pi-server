from servo import servo_angle, mid_servo, min_servo, max_servo
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

DEGREES = 360


def get_medicine(position):
    print(position)


#  mid_servo()
#  sleep(1)
#  step_forward(DEGREES)
#  sleep(1)
#  max_servo()
#  sleep(1)
#  step_backward(DEGREES)
