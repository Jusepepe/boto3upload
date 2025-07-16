from controlESP import moveForward, moveBack, checkLimitSwitch, returnToInitialPosition
import time

while not checkLimitSwitch()[1]:
    moveForward()
    time.sleep(1)

returnToInitialPosition()
