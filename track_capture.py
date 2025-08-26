from controllers.camera_controller import Camera
from controllers.boto_controller import upload_fileobj
from controllers.esp_controller import get_forward_controller, get_backward_controller
import time

camera_1: Camera = Camera(0)
camera_2: Camera = Camera(1)

def capture_image():
    data_1 = camera_1.capture_image()
    data_2 = camera_2.capture_image()
    return data_1, data_2

def upload_images(data_1, data_2, path, direction):
    upload_fileobj(data_1, bucket_name, path + "front/" + direction + ".png")
    upload_fileobj(data_2, bucket_name, path + "back/" + direction + ".png")

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
bucket_name: str = 'citric-bucket'
initial_track: int = 1

forward_controller = get_forward_controller()
backward_controller = get_backward_controller()

time.sleep(1)

try:
    while not int(forward_controller.check_limit_switch()):
        if initial_track == 6:
            break
        print("Track:", initial_track)
        track = "Track_" + str(initial_track)
        path: str = day + "/raw/" + hour + "/" + track + "/"
        data_1, data_2 = capture_image()
        upload_images(data_1, data_2, path, "middle")
        initial_track += 1
        forward_controller.step(2000)
        time.sleep(1)

    backward_controller.step(25000)
except KeyboardInterrupt:
    pass
finally:
    print("Subida de archivos terminada")