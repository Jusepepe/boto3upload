import io
class CameraMock():
    def __init__(self, camera_id: int):
        self.camera_id = camera_id

    def capture_image(self):
        print("Capturing image with camera", self.camera_id)
        id = ("camera_" + str(self.camera_id)).encode('utf-8')
        data = io.BytesIO(id)
        data.seek(0)
        return data