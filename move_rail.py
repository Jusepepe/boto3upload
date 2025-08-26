from controllers.esp_controller import get_forward_controller, get_backward_controller
import time

forward_controller = get_forward_controller()
backward_controller = get_backward_controller()

state0 = int(forward_controller.check_limit_switch())
state1 = int(backward_controller.check_limit_switch())
states = [state0, state1]
print(states)

while not (state0 == 1):
    print(state0)
    forward_controller.step(2000)
    time.sleep(1)
    state0 = int(forward_controller.check_limit_switch())

print(state0)
backward_controller.step(25000)
