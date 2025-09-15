"""
Camera Controller

This module provides an interface to control the Raspberry Pi camera.
It handles camera initialization, configuration, and image capture.
"""

import io
import logging
from time import sleep
from typing import BinaryIO

try:
    from picamera2 import Picamera2
    PICAMERA_AVAILABLE = True
except ImportError:
    PICAMERA_AVAILABLE = False
    logging.warning("Picamera2 not available. Using mock implementation.")


class Camera:
    """A class to control the Raspberry Pi camera."""
    
    def __init__(self, camera_id: int = 0, width: int = 4056, height: int = 3040):
        if not PICAMERA_AVAILABLE:
            raise RuntimeError("Picamera2 is not available on this system.")
            
        self.picam2 = Picamera2(camera_id)
        self.config = self.picam2.create_still_configuration(
            main={"format": "RGB888", "size": (width, height)}
        )
        self.picam2.configure(self.config)

    def capture_image(self) -> BinaryIO:
        """Capture an image and return it as a BytesIO object."""
        try:
            self.picam2.start()
            sleep(1)  # Allow camera to warm up
            data = io.BytesIO()
            self.picam2.switch_mode_and_capture_file(self.config, data, format='png', delay=5)
            data.seek(0)
            return data
        finally:
            self.picam2.stop()

    def capture_image_low_res(self) -> BinaryIO:
        """Capture an image with lower resolution and return it as a BytesIO object."""
        try:
            low_res_config = self.picam2.create_still_configuration(
                main={"format": "RGB888", "size": (720, 480)}
            )
            self.picam2.configure(low_res_config)
            self.picam2.start()
            sleep(1)  # Allow camera to warm up
            data = io.BytesIO()
            self.picam2.switch_mode_and_capture_file(low_res_config, data, format='png', delay=5)
            data.seek(0)
            return data
        finally:
            self.picam2.stop()

    def __del__(self):
        """Ensure camera resources are properly released."""
        if hasattr(self, 'picam2') and self.picam2 is not None:
            self.picam2.close()
