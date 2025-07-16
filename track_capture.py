from moveServos import complete_sequence, capture_image, reset_servos, upload_images
from controlESP import moveForward, moveBack, checkLimitSwitch
import time

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
bucket_name: str = 'citric-bucket'
initial_track: int = 1

last_track: int = 6

time.sleep(1)
reset_servos()

try:
    while initial_track <= last_track:
        print("Track:", initial_track)
        track = "Track_" + str(initial_track)
        path: str = day + "/raw/" + hour + "/" + track + "/"
        for i, sequence in enumerate(complete_sequence):
            tilt, pan = sequence()
            direction = tilt + "_" + pan

            print("N°", i)
            print("Direction:", direction)
            data_1, data_2 = capture_image()
            upload_images(data_1, data_2, path, direction)
        initial_track += 1
        moveBack()
        time.sleep(1)

    while not checkLimitSwitch()[0]:
        moveForward()
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    print("Subida de archivos terminada")