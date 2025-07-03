import ServoController

class PanTilt:
    def __init__(self, pan_pin, tilt_pin):
        self.pan = ServoController(pan_pin)
        self.tilt = ServoController(tilt_pin)

    def sweep_pan_left(self):
        self.pan.sweep_to(0)

    def sweep_pan_right(self):
        self.pan.sweep_to(180)

    def sweep_pan_center(self):
        self.pan.sweep_to(90)

    def sweep_tilt_up(self):
        self.tilt.sweep_to(180)

    def sweep_tilt_three_quarter_up(self):
        self.tilt.sweep_to(150)

    def sweep_tilt_quarter_up(self):
        self.tilt.sweep_to(120)

    def cleanup(self):
        self.pan.cleanup()
        self.tilt.cleanup()