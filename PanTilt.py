import ServoController

class PanTilt:
    def __init__(self, pan_pin, tilt_pin):
        self.pan = ServoController(pan_pin)
        self.tilt = ServoController(tilt_pin)

    def set_pan(self, angle):
        self.pan.set_angle(angle)

    def set_tilt(self, angle):
        self.tilt.set_angle(angle)

    def cleanup(self):
        self.pan.cleanup()
        self.tilt.cleanup()