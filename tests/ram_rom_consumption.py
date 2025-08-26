import os
import time
import psutil
import tracemalloc
from pathlib import Path
from cv_models.base import ObjectDetectionModel
from cv_models.yolo_11s import Yolo11s
from controllers.camera_controller import Camera

# ------------------------
# Memory Profiler
# ------------------------
class MemoryProfiler:
    def __init__(self):
        self.process = psutil.Process(os.getpid())

    def get_ram_usage(self):
        """Current RAM usage in MB"""
        return self.process.memory_info().rss / (1024**2)

    def get_rom_usage(self, path="."):
        """Disk usage of given directory in MB"""
        usage = 0
        for root, _, files in os.walk(path):
            for f in files:
                fp = os.path.join(root, f)
                usage += os.path.getsize(fp)
        return usage / (1024**2)

    def monitor_inference(self, model: ObjectDetectionModel, image_data: bytes):
        # Before inference
        ram_before = self.get_ram_usage()
        rom_before = self.get_rom_usage()

        # Start tracemalloc for Python allocations
        tracemalloc.start()

        start = time.time()
        result = model.process(image_data)
        end = time.time()

        # After inference
        ram_after = self.get_ram_usage()
        rom_after = self.get_rom_usage()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        report = {
            "RAM_before_MB": ram_before,
            "RAM_after_MB": ram_after,
            "RAM_peak_MB": peak / (1024**2),
            "ROM_before_MB": rom_before,
            "ROM_after_MB": rom_after,
            "Inference_time_sec": end - start
        }
        return report


# ------------------------
# Example Run
# ------------------------
if __name__ == "__main__":
    model = Yolo11s()
    profiler = MemoryProfiler()

    cam = Camera(0)
    image_data = cam.capture_image()
    report = profiler.monitor_inference(model, image_data)

    print("\n--- Inference Memory Report ---")
    for k, v in report.items():
        if isinstance(v, float):
            print(f"{k}: {v:.4f}")
        else:
            print(f"{k}: {v}")
