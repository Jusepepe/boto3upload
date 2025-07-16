from controlESP import moveForward, moveBack, checkLimitSwitch, returnToInitialPosition
import time

while not checkLimitSwitch()[0]:
    print("Moviendo hacia adelante")
    moveForward()
    time.sleep(1)

print("Moviendo al inicio")
returnToInitialPosition()
