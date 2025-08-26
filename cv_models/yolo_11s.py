from .base import ObjectDetectionModel
from ultralytics import YOLO
from PIL import Image

class Yolo11s(ObjectDetectionModel):
    def __init__(self):
        super().__init__()
        self.model = YOLO("cv_models/weights/my_yolo11s.pt")
    
    def process(self, image_data: bytes):
        image_data = Image.open(image_data).convert("RGB")
        results = self.model.predict(image_data)
        return results