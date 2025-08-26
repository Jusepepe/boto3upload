import time
import sys
import PIL
import io
from controllers.camera_controller import Camera
from controllers.boto_controller import upload_fileobj
from cv_models.base import ObjectDetectionModel
from cv_models import RTDETR, Yolo11s

# ------------------------
# Latency Timer
# ------------------------
class LatencyTimer:
    def __init__(self):
        self.timestamps = {}

    def mark(self, label: str):
        self.timestamps[label] = time.time()

    def report(self):
        keys = list(self.timestamps.keys())
        report = {}
        for i in range(1, len(keys)):
            prev, curr = keys[i-1], keys[i]
            report[f"{prev} → {curr}"] = self.timestamps[curr] - self.timestamps[prev]
        report["Total"] = self.timestamps[keys[-1]] - self.timestamps[keys[0]]
        return report


# ------------------------
# Main Pipeline
# ------------------------
def run_pipeline(model: ObjectDetectionModel, bucket_name: str, camera_ids: list):
    timer = LatencyTimer()

    # Step 1: Capture
    for camera_id in camera_ids:
        cam = Camera(camera_id)
        timer.mark("start_capture_camera_"+str(camera_id))
        image_data = cam.capture_image()  # get PNG bytes
        timer.mark("end_capture_camera_"+str(camera_id))

        # Step 2: Upload
        upload_fileobj(image_data, bucket_name, "test/image-captured_"+str(camera_id)+".png")
        timer.mark("end_upload_camera_"+str(camera_id))

        # Step 3: Inference
        results = model.process(image_data)
        timer.mark("end_inference_camera_"+str(camera_id))

        # Step 4: Upload Inference
        annotated_image = results[0].plot()
        annotated_image = PIL.Image.fromarray(annotated_image)
        image_data = io.BytesIO()
        annotated_image.save(image_data, "PNG")
        image_data.seek(0)
        upload_fileobj(image_data, bucket_name, "test/image-inference_"+str(camera_id)+".png")
        timer.mark("end_upload_inference_camera_"+str(camera_id))

    # Step 5: Report
    print("\n--- Latency Report ---")
    for step, latency in timer.report().items():
        print(f"{step}: {latency:.4f} sec")

# ------------------------
# Run Example
# ------------------------
if __name__ == "__main__":
    bucket = "citric-bucket"

    args = sys.argv
    model = args[1]
    if model == "yolo11s":
        model = Yolo11s()
    elif model == "rtdetr":
        model = RTDETR()
    run_pipeline(model, bucket, camera_ids=[0, 1])
