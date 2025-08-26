import time
from controllers.camera_controller import Camera
from controllers.boto_controller import upload_fileobj
from cv_models.base import ObjectDetectionModel
from cv_models.dummy_yolo import DummyYOLO

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

    # Step 4: Report
    print("\n--- Latency Report ---")
    for step, latency in timer.report().items():
        print(f"{step}: {latency:.4f} sec")

    print("\n--- Results ---")
    print("Results:", results)


# ------------------------
# Run Example
# ------------------------
if __name__ == "__main__":
    bucket = "citric-bucket"
    model = DummyYOLO()
    run_pipeline(model, bucket, camera_ids=[0, 1])
