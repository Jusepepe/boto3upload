from servo_controller_mock import ServoControllerMock

class PanTiltMock:
    def __init__(self, pan_pin, tilt_pin):
        self.pan = ServoControllerMock(pan_pin)
        self.tilt = ServoControllerMock(tilt_pin)
    
    def reset(self):
        self.pan.set_angle(90)
        self.tilt.set_angle(90)
    
    def cleanup(self):
        self.pan.cleanup()
        self.tilt.cleanup()
