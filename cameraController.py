from picamera2 import Picamera2
import io
from time import sleep

def capture_image():
    picam2 = Picamera2()
    picam2.start()
    sleep(1)
    data = io.BytesIO()
    picam2.capture_files(data, format='jpeg')
    return data