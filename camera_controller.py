from picamera2 import Picamera2
import io
from time import sleep

class Camera():

    def __init__(self, camera_id: int):
        self.picam2 = Picamera2(camera_id)
        self.config = self.picam2.create_still_configuration(main={"format": "RGB888", "size": (4056, 3040)})
        self.picam2.configure(self.config)

    def capture_image(self):
        self.picam2.start()
        sleep(1)
        data = io.BytesIO()
        self.picam2.capture_file(data, format='png')
        data.seek(0)
        self.picam2.stop()
        return data
