from picamera2 import Picamera2
from picamera2.previews.drpreview import DRMPreview
import time

picam2 = Picamera2()
preview = DRMPreview()
picam2.start_preview(preview)
picam2.start()

time.sleep(10)  # Preview durante 10 segundos

picam2.stop()
