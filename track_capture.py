from moveServos import complete_sequence, capture_image, reset_servos, upload_images
from controlESP import moveForward, moveBack, checkLimitSwitch, returnToInitialPosition
import time

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
bucket_name: str = 'citric-bucket2'
initial_track: int = 1

time.sleep(1)
reset_servos()

try:
    while not int(checkLimitSwitch()[0]):
        print("Track:", initial_track)
        track = "Track_" + str(initial_track)
        path: str = day + "/raw/" + hour + "/" + track + "/"
        upload_images(data_1, data_2, path, "middle")
        initial_track += 1
        moveForward()
        time.sleep(1)

    returnToInitialPosition()
except KeyboardInterrupt:
    pass
finally:
    print("Subida de archivos terminada")