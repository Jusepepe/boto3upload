from PanTilt import PanTilt
import time

pan_tilt_1: PanTilt = PanTilt(17, 27)
pan_tilt_2: PanTilt = PanTilt(25, 24)

def reset_servos():
    pan_tilt_1.pan.set_angle(75)
    pan_tilt_2.pan.set_angle(80)
    pan_tilt_1.tilt.set_angle(200)
    pan_tilt_2.tilt.set_angle(145)

def move_left():
    pan_tilt_1.pan.sweep_to(95)
    pan_tilt_2.pan.sweep_to(60)
    pan = "Left"
    return pan

def move_center():
    pan_tilt_1.pan.sweep_to(75)
    pan_tilt_2.pan.sweep_to(80)
    pan = "Center"
    return pan

def move_right():
    pan_tilt_1.pan.sweep_to(45)
    pan_tilt_2.pan.sweep_to(100)
    pan = "Right"
    return pan

def move_up():
    pan_tilt_1.tilt.sweep_to(200)
    pan_tilt_2.tilt.sweep_to(145)
    tilt = "Up"
    return tilt

def move_quarter_up():
    pan_tilt_1.tilt.sweep_to(175)
    pan_tilt_2.tilt.sweep_to(125)
    tilt = "Quarter Up"
    return tilt
def move_three_quarter_up():
    pan_tilt_1.tilt.sweep_to(150)
    pan_tilt_2.tilt.sweep_to(100)
    tilt = "Three Quarter Up"
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

def lower_sequence_left() -> list:
    return [move_three_quarter_up(), move_left()]

def lower_sequence_center() -> list:
    return [move_three_quarter_up(), move_center()]

def lower_sequence_right() -> list:
    return [move_three_quarter_up(), move_right()]

complete_sequence : list = [upper_sequence_left, upper_sequence_center, upper_sequence_right, middle_sequence_right, middle_sequence_center, middle_sequence_left, lower_sequence_left, lower_sequence_center, lower_sequence_right]

reset_servos()

for i, sequence in enumerate(complete_sequence):
    tilt, pan = sequence()
    direction = tilt + "_" + pan

    print("N°", i)
    print("Direction:", direction)
    time.sleep(5)

pan_tilt_1.cleanup()
pan_tilt_2.cleanup()


