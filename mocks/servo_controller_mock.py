"""
Mock Servo Controller

This module provides a mock implementation of a servo controller for testing purposes.
It simulates servo movements without requiring actual hardware.
"""

import time
import logging
from typing import Optional


class ServoControllerMock:
    """Mock implementation of a servo controller for testing.
    
    This class simulates the behavior of a servo motor controller without
    requiring actual hardware. It's useful for testing and development.
    
    Args:
        pin: The GPIO pin number (unused in mock)
        min_angle: Minimum angle in degrees (default: 0)
        max_angle: Maximum angle in degrees (default: 180)
        initial_angle: Starting angle in degrees (default: 90)
    """
    
    def __init__(
        self,
        pin: int,
        min_angle: float = 0.0,
        max_angle: float = 180.0,
        initial_angle: float = 90.0
    ):
        self.pin = pin
        self.min_angle = min(min_angle, max_angle)
        self.max_angle = max(min_angle, max_angle)
        self.current_angle = max(min(initial_angle, self.max_angle), self.min_angle)
        self._is_cleanup = False
        logging.info(
            "Initialized mock servo controller on pin %d (angle range: %.1f° to %.1f°)",
            pin, self.min_angle, self.max_angle
        )
    
    def set_angle(self, angle: float) -> None:
        """Set the servo to a specific angle.
        
        Args:
            angle: Desired angle in degrees (will be clamped to min/max range)
        """
        if self._is_cleanup:
            logging.warning("Attempted to set angle after cleanup")
            return
            
        clamped_angle = max(self.min_angle, min(angle, self.max_angle))
        if clamped_angle != angle:
            logging.warning("Angle %.1f° clamped to %.1f°", angle, clamped_angle)
            
        self.current_angle = clamped_angle
        logging.debug("Set servo angle to %.1f°", self.current_angle)
    
    def sweep_to(
        self,
        target_angle: float,
        step: float = 1.0,
        delay: float = 0.01
    ) -> None:
        """Smoothly move the servo to the target angle.
        
        Args:
            target_angle: Target angle in degrees
            step: Step size in degrees for each movement
            delay: Delay in seconds between steps
        """
        if self._is_cleanup:
            logging.warning("Attempted to sweep after cleanup")
            return
            
        target_angle = max(self.min_angle, min(target_angle, self.max_angle))
        step = abs(step) if target_angle >= self.current_angle else -abs(step)
        
        logging.info("Sweeping from %.1f° to %.1f° (step: %.1f°)",
                    self.current_angle, target_angle, step)
        
        # Generate angle sequence
        angles = []
        current = self.current_angle
        while (step > 0 and current < target_angle) or (step < 0 and current > target_angle):
            current += step
            if (step > 0 and current > target_angle) or (step < 0 and current < target_angle):
                current = target_angle
            angles.append(current)
        
        # Execute the movement
        for angle in angles:
            self.set_angle(angle)
            time.sleep(delay)
    
    def cleanup(self) -> None:
        """Clean up resources and disable the servo."""
        if not self._is_cleanup:
            logging.info("Cleaning up mock servo controller on pin %d", self.pin)
            self._is_cleanup = True
    
    def __del__(self):
        """Ensure cleanup is called when the object is destroyed."""
        self.cleanup()
