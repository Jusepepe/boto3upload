from controlESP import moveForward, moveBack, checkLimitSwitch, returnToInitialPosition
import time

while not checkLimitSwitch()[1]:
    print("Moviendo hacia adelante")
    moveForward()
    time.sleep(1)

print("Moviendo al inicio")
returnToInitialPosition()
