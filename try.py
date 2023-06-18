from nema_stepper import stepper_x_cw, stepper_x_ccw, stepper_y_cw, stepper_y_ccw
from stepper import back_movement, front_movement, step_b_backward, step_b_forward, step_f_forward, step_f_backward
from time import sleep

def axis_movement(x_steps = 200, y_steps=200):
    stepper_x_cw(x_steps)
    sleep(1)
    stepper_y_cw(y_steps)
    sleep(1)
    # front_movement()
    # sleep(1)
    stepper_x_ccw(x_steps)
    sleep(1)
    stepper_y_ccw(y_steps)
    sleep(1)
    # back_movement()
    # sleep(1)

# axis_movement(2000, 2000)
# while(True):
    # stepper_x_cw(2000)
    # stepper_x_ccw(2000)
# while(True):
# stepper_y_cw(650) #up
# sleep(10)
# stepper_y_ccw(650) # down
# back_movement()


# sleep(1)
# front_movement()
# step_f_forward(30)

# stepper_y_cw(720)
# stepper_y_cw(720)

stepper_y_cw(700)
# sleep(5)
# front_movement()

# back_movement()
# sleep(5)
# stepper_y_ccw(700)

# sleep(5)

# step_b_forward(150)