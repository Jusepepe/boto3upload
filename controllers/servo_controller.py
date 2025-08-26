"""Servo controller for hardware control."""

import logging
import RPi.GPIO as GPIO
import time

class ServoController:
    """Controls a servo motor via GPIO."""
    
    def __init__(self, pin: int, min_angle: float = 0, max_angle: float = 180):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)
        self.current_angle = None
        logging.info(f"Initialized servo on pin {pin}")
    
    def set_angle(self, angle: float) -> None:
        """Set servo angle."""
        duty_cycle = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
        self.pwm.ChangeDutyCycle(0)
        self.current_angle = angle
        logging.debug(f"Set angle to {self.current_angle}°")
    
    def sweep_to(self, target_angle, step=5):
        target_angle = max(0, min(200, target_angle))
        sign = 1
        if target_angle < self.current_angle:
            sign = -1
        for angle in range(self.current_angle, target_angle + sign, step*sign):
            self.set_angle(angle)
            time.sleep(0.4)
        logging.debug(f"Swept to angle {self.current_angle}°")

    def cleanup(self) -> None:
        """Clean up GPIO resources."""
        logging.info("Cleaning up servo controller")
        self.current_angle = None
