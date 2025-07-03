from picamera2 import Picamera2
import io
from time import sleep

class Camera():

    def __init__(self, camera_id: int):
        self.picam2 = Picamera2(camera_id)

    def capture_image(self):
        self.picam2.start()
        sleep(1)
        data = io.BytesIO()
        self.picam2.capture_file(data, format='jpeg')
        data.seek(0)
        self.picam2.stop()
        return data