from .base import ObjectDetectionModel
from ultralytics import RTDETR as UltralyticsRTDETR
from PIL import Image

class RTDETR(ObjectDetectionModel):
    def __init__(self):
        super().__init__()
        self.model = UltralyticsRTDETR("cv_models/weights/rtdetr.pt")
    
    def process(self, image_data: bytes):
        image_data = Image.open(image_data).convert("RGB")
        results = self.model.predict(image_data)
        return results
