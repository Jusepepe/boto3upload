import time
class ServoControllerMock:
    def __init__(self, pin):
        self.pin = pin
        self.current_angle = None    
    
    def set_angle(self, angle):
        print("Setting angle to", angle)
        self.current_angle = angle
    
    def sweep_to(self, target_angle, step=1):
        target_angle = max(0, min(180, target_angle))
        if target_angle < self.current_angle:
            step = -step
        for angle in range(self.current_angle, target_angle + 1, step):
            self.set_angle(angle)
            time.sleep(0.01)
    
    def cleanup(self):
        pass