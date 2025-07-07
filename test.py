from PanTilt import PanTilt
import time

pan_tilt_1: PanTilt = PanTilt(17, 27)
pan_tilt_2: PanTilt = PanTilt(25, 24)

pan1_center = 75
pan2_center = 80
tilt1_up = 200
tilt2_up = 145
tilt1_quarter_up = 175
tilt2_quarter_up = 125
tilt1_three_quarter_up = 160
tilt2_three_quarter_up = 100

def reset_servos():
    pan_tilt_1.pan.set_angle(pan1_center)
    pan_tilt_2.pan.set_angle(pan2_center)
    pan_tilt_1.tilt.set_angle(tilt1_quarter_up)
    pan_tilt_2.tilt.set_angle(tilt2_quarter_up)

def move_left():
    pan_tilt_1.pan.set_angle(95)
    pan_tilt_2.pan.set_angle(55)
    pan = "Left"
    return pan

def move_center():
    pan_tilt_1.pan.set_angle(pan1_center)
    pan_tilt_2.pan.set_angle(pan2_center)
    pan = "Center"
    return pan

def move_right():
    pan_tilt_1.pan.set_angle(35)
    pan_tilt_2.pan.set_angle(110)
    pan = "Right"
    return pan

def move_up():
    pan_tilt_1.tilt.set_angle(tilt1_up)
    pan_tilt_2.tilt.set_angle(tilt2_up)
    tilt = "Up"
    return tilt

def move_quarter_up():
    pan_tilt_1.tilt.set_angle(tilt1_quarter_up)
    pan_tilt_2.tilt.set_angle(tilt2_quarter_up)
    tilt = "Quarter Up"
    return tilt

def upper_sequence_left() -> list:
    return [move_up(), move_left()]

def upper_sequence_center() -> list:
    return [move_up(), move_center()]

def upper_sequence_right() -> list:
    return [move_up(), move_right()]

def middle_sequence_right() -> list:
    return [move_quarter_up(), move_right()]

def middle_sequence_center() -> list:
    return [move_quarter_up(), move_center()]

def middle_sequence_left() -> list:
    return [move_quarter_up(), move_left()]

complete_sequence : list = [upper_sequence_left, upper_sequence_center, upper_sequence_right, middle_sequence_right, middle_sequence_center, middle_sequence_left]

reset_servos()

for i, sequence in enumerate(complete_sequence):
    tilt, pan = sequence()
    direction = tilt + "_" + pan

    print("N°", i)
    print("Direction:", direction)
    time.sleep(1)



