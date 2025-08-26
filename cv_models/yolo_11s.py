import time
from .base import ObjectDetectionModel
from ultralytics import YOLO

class Yolo11s(ObjectDetectionModel):
    def process(self, image_data: bytes):
        model = YOLO("cv_models/weights/my_yolo11s.pt")
        results = model.predict(image_data)
        return results