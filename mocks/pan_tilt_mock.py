"""Mock Pan-Tilt Controller for testing camera mount movements."""

import logging
from typing import Tuple
from .servo_controller_mock import ServoControllerMock


class PanTiltMock:
    """Mock pan-tilt mechanism with pan and tilt servos."""
    
    def __init__(
        self,
        pan_pin: int,
        tilt_pin: int,
        pan_range: Tuple[float, float] = (0, 180),
        tilt_range: Tuple[float, float] = (0, 180),
        initial_position: Tuple[float, float] = (90, 90)
    ):
        self.pan = ServoControllerMock(pan_pin, *pan_range, initial_position[0])
        self.tilt = ServoControllerMock(tilt_pin, *tilt_range, initial_position[1])
        logging.info("Initialized mock pan-tilt controller")
    
    def reset(self) -> None:
        """Reset to center position."""
        self.pan.set_angle(90)
        self.tilt.set_angle(90)
    
    def set_position(self, pan: float, tilt: float) -> None:
        """Set pan and tilt angles."""
        self.pan.set_angle(pan)
        self.tilt.set_angle(tilt)
    
    def get_position(self) -> Tuple[float, float]:
        """Get current pan and tilt angles."""
        return self.pan.current_angle, self.tilt.current_angle
    
    def cleanup(self) -> None:
        """Clean up resources."""
        self.pan.cleanup()
        self.tilt.cleanup()
    
    def __del__(self):
        self.cleanup()
