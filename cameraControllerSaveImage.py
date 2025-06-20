import time

from picamera2 import Picamera2, Preview

picam1 = Picamera2(0)
picam2 = Picamera2(1)
picam1.start_preview(Preview.QT)
picam2.start_preview(Preview.QT)

preview_config1 = picam1.create_preview_configuration()
preview_config2 = picam2.create_preview_configuration()
picam1.configure(preview_config1)
picam2.configure(preview_config2)

picam1.start()
picam2.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    picam1.stop()
    picam2.stop()
    

