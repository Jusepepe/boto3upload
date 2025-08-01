from picamera2 import Picamera2
from picamera2.previews.gl_preview import GLPreview
import time

picam2 = Picamera2()
preview = GLPreview()
picam2.start_preview(preview)
picam2.start()

time.sleep(10)

picam2.stop()
