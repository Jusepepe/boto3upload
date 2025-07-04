from PanTilt import PanTilt
import sys

pan_tilt_1: PanTilt = PanTilt(17, 27)
pan_tilt_2: PanTilt = PanTilt(23, 24)

args = sys.argv

print(args)
pan_tilt_1.pan.set_angle(int(args[1]))
pan_tilt_2.pan.set_angle(int(args[2]))
pan_tilt_1.tilt.set_angle(int(args[3]))
pan_tilt_2.tilt.set_angle(int(args[4]))

