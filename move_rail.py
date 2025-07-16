from controlESP import moveForward, moveBack, checkLimitSwitch, returnToInitialPosition
import time

state0 = int(checkLimitSwitch()[0])
state1 = int(checkLimitSwitch()[1])
states = [state0, state1]
print(states)

while not (state0 := int(checkLimitSwitch()[0])):
    print(state0)
    moveForward()
    time.sleep(1)

print(state0)
returnToInitialPosition()
