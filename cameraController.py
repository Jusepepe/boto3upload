from picamera2 import Picamera2
import io
from time import sleep

class Camera():
    _instance = None

    def __new__(cls):
        if Camera._instance is None:
            Camera._instance = Picamera2()

        return Camera._instance

def capture_image():
    picam2 = Camera()
    
    picam2.start()
    sleep(1)
    data = io.BytesIO()
    picam2.capture_file(data, format='jpeg')
    data.seek(0)
    return data