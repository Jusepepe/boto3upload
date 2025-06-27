import PanTilt
import sys

pan_tilt_1 = PanTilt(17, 18)
pan_tilt_2 = PanTilt(27, 22)

args = sys.argv

if len(args) < 3:
    print("Usage: python moveServos.py <pan_angle> <tilt_angle>")
    sys.exit(1)

pan_angle = int(args[1])
tilt_angle = int(args[2])

pan_tilt_1.set_pan(pan_angle)
pan_tilt_1.set_tilt(tilt_angle)
pan_tilt_2.set_pan(pan_angle)
pan_tilt_2.set_tilt(tilt_angle)

pan_tilt_1.cleanup()
pan_tilt_2.cleanup()

