"""Pan-tilt controller for camera mount."""

import logging
from typing import Tuple
from .servo_controller import ServoController


class PanTilt:
    """Controls a pan-tilt mechanism with two servos."""
    
    def __init__(
        self,
        pan_pin: int,
        tilt_pin: int,
        pan_range: Tuple[float, float] = (0, 180),
        tilt_range: Tuple[float, float] = (0, 180),
        initial_position: Tuple[float, float] = (90, 90)
    ):
        self.pan = ServoController(pan_pin, *pan_range)
        self.tilt = ServoController(tilt_pin, *tilt_range)
        self.set_position(*initial_position)
        logging.info("Initialized pan-tilt controller")
    
    def set_position(self, pan: float, tilt: float) -> None:
        """Set pan and tilt angles."""
        self.pan.set_angle(pan)
        self.tilt.set_angle(tilt)
    
    def get_position(self) -> Tuple[float, float]:
        """Get current pan and tilt angles."""
        return self.pan.current_angle, self.tilt.current_angle
    
    def reset(self) -> None:
        """Reset to center position."""
        self.set_position(90, 90)
    
    def cleanup(self) -> None:
        """Clean up resources."""
        self.pan.cleanup()
        self.tilt.cleanup()
    
    def __del__(self):
        self.cleanup()
