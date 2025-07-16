import io
import cv2
class CameraMock():
    def __init__(self, camera_id: int):
        self.camera_id = camera_id

    def capture_image(self):
        print("Capturing image with camera", self.camera_id)
        image = cv2.imread("aphid.01.jpg")
        is_success, buffer = cv2.imencode(".jpg", image)
        data = io.BytesIO(buffer)
        data.seek(0)
        return data