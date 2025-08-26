import time
from .base import ObjectDetectionModel

class DummyYOLO(ObjectDetectionModel):
    def process(self, image_data: bytes):
        time.sleep(0.5)  # simulate processing delay
        return {"detections": [{"class": "person", "confidence": 0.91}]}
