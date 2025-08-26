from .base import ObjectDetectionModel
from ultralytics import RTDETR
from PIL import Image

class RTDETR(ObjectDetectionModel):
    def __init__(self):
        super().__init__()
        self.model = RTDETR("cv_models/weights/my-rtdetr.pt")
    
    def process(self, image_data: bytes):
        image_data = Image.open(image_data).convert("RGB")
        results = self.model.predict(image_data)
        return results
