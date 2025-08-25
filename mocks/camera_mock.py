"""
Mock Camera Implementation

This module provides a mock implementation of the Camera class for testing purposes.
It simulates camera behavior without requiring actual hardware.
"""

import io
import os
from typing import BinaryIO, Optional
import logging
import cv2
import numpy as np


class CameraMock:
    """Mock implementation of a camera for testing.
    
    Args:
        camera_id: Camera identifier (unused in mock)
        test_image_path: Path to a test image to use. If not provided,
                        generates a simple colored image.
    """
    
    def __init__(self, camera_id: int = 0, test_image_path: Optional[str] = None):
        self.camera_id = camera_id
        self.test_image_path = test_image_path
        self.is_open = False
        self._setup_test_image()
        
    def _setup_test_image(self):
        """Set up the test image to be used for captures."""
        if self.test_image_path and os.path.exists(self.test_image_path):
            self.test_image = cv2.imread(self.test_image_path)
            if self.test_image is None:
                logging.warning("Failed to load test image, using default pattern")
                self._generate_test_pattern()
        else:
            self._generate_test_pattern()
    
    def _generate_test_pattern(self):
        """Generate a simple test pattern if no test image is available."""
        # Create a simple gradient pattern
        height, width = 3040, 4056
        gradient = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            gradient[y, :, 0] = int(255 * y / height)  # Blue
            gradient[y, :, 1] = int(255 * (1 - y / height))  # Green
            gradient[y, :, 2] = 128  # Red
        self.test_image = gradient

    def capture_image(self) -> BinaryIO:
        """Simulate capturing an image.
        
        Returns:
            BinaryIO: A file-like object containing the image data in PNG format.
        """
        logging.info("Mock: Capturing image with camera %s", self.camera_id)
        
        # Convert to RGB (from BGR which OpenCV uses)
        rgb_image = cv2.cvtColor(self.test_image, cv2.COLOR_BGR2RGB)
        
        # Encode as PNG in memory
        success, buffer = cv2.imencode(".png", rgb_image)
        if not success:
            raise RuntimeError("Failed to encode test image")
            
        # Convert to file-like object
        data = io.BytesIO(buffer)
        data.seek(0)
        return data
    
    def __del__(self):
        """Clean up resources."""
        self.is_open = False
