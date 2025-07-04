from ServoController import ServoController

class PanTilt:
    def __init__(self, pan_pin, tilt_pin):
        self.pan = ServoController(pan_pin)
        self.tilt = ServoController(tilt_pin)

    def cleanup(self):
        self.pan.cleanup()
        self.tilt.cleanup()