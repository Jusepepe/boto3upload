from moveServos import complete_sequence, capture_image, reset_servos, upload_images
from controlESP import moveForward, moveBack
import time

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
bucket_name: str = 'citric-bucket'
track_list: list = [1,2,3,4,5,6,7]

time.sleep(1)
reset_servos()

for track in track_list:
    path: str = day + "/raw/" + hour + "/Track_"+str(track)+"/"
    for i, sequence in enumerate(complete_sequence):
        tilt, pan = sequence()
        direction = tilt + "_" + pan

        print("N°", i)
        print("Direction:", direction)
        data_1, data_2 = capture_image()
        upload_images(data_1, data_2, path, direction)

    moveForward()
    time.sleep(1)
