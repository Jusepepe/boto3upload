from picamera2 import Picamera2
import cv2

picam2 = Picamera2(1)

# Crear configuración para vista previa
config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()

while True:
    frame = picam2.capture_array()
    cv2.imshow("Vista previa", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
