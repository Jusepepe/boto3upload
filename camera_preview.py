from picamera2 import Picamera2
from picamera2.previews.qt import QGlPicamera2
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

picam2 = Picamera2()
preview = QGlPicamera2(picam2, width=640, height=480)
preview.show()

picam2.start()
app.exec()
