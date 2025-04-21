from picamera2 import Picamera2
import io
from time import sleep

picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
picam2.start(show_preview=True)
sleep(1)
picam2.switch_mode_and_capture_file(capture_config, "image.jpg")