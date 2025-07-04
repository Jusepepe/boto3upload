import RPi.GPIO as GPIO
import time

class ServoController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)
        self.current_angle = None

    def set_angle(self, angle):
        print("Setting angle to", angle)
        duty_cycle = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
        self.pwm.ChangeDutyCycle(0)
        self.current_angle = angle

    def sweep_to(self, target_angle, step=10):
        target_angle = max(0, min(180, target_angle))
        if target_angle < self.current_angle:
            step = -step
        for angle in range(self.current_angle, target_angle + 1, step):
            self.set_angle(angle)
            time.sleep(0.1)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()