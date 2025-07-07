from PanTilt import PanTilt
import time

pan_tilt_1: PanTilt = PanTilt(17, 27)
pan_tilt_2: PanTilt = PanTilt(25, 24)

is_up = False
is_quarter_up = False

pan1 = {"left": 100, "center": 75, "right": 30}
pan2 = {"left": 50, "center": 80, "right": 110}
tilt1 = {"up": 198, "quarter_up": 175}
tilt2 = {"up": 140, "quarter_up": 125}

def reset_servos():
    pan_tilt_1.pan.set_angle(pan1["center"])
    time.sleep(1)
    pan_tilt_2.pan.set_angle(pan2["center"])
    time.sleep(1)
    pan_tilt_1.tilt.set_angle(tilt1["up"])
    time.sleep(1)
    pan_tilt_2.tilt.set_angle(tilt2["up"])
    time.sleep(1)

def move_left():
    pan_tilt_1.pan.sweep_to(pan1["left"])
    time.sleep(1)
    pan_tilt_2.pan.sweep_to(pan2["right"])
    time.sleep(1)
    pan = "Left"
    return pan

def move_center():
    pan_tilt_1.pan.sweep_to(pan1["center"])
    time.sleep(1)
    pan_tilt_2.pan.sweep_to(pan2["center"])
    time.sleep(1)
    pan = "Center"
    return pan

def move_right():
    pan_tilt_1.pan.sweep_to(pan1["right"])
    time.sleep(1)
    pan_tilt_2.pan.sweep_to(pan2["left"])
    time.sleep(1)
    pan = "Right"
    return pan

def move_up():
    global is_up
    if is_up:
        return "Up"
    pan_tilt_1.tilt.sweep_to(tilt1["up"])
    time.sleep(1)
    pan_tilt_2.tilt.sweep_to(tilt2["up"])
    time.sleep(1)
    tilt = "Up"
    is_up = True
    is_quarter_up = False
    return tilt

def move_quarter_up():
    global is_quarter_up
    if is_quarter_up:
        return "Quarter Up"
    pan_tilt_1.tilt.sweep_to(tilt1["quarter_up"])
    time.sleep(1)
    pan_tilt_2.tilt.sweep_to(tilt2["quarter_up"])
    time.sleep(1)
    tilt = "Quarter Up"
    is_quarter_up = True
    is_up = False
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

complete_sequence : list = [upper_sequence_left, upper_sequence_center, upper_sequence_right, middle_sequence_left, middle_sequence_center, middle_sequence_right]

reset_servos()

for i, sequence in enumerate(complete_sequence):
    tilt, pan = sequence()
    direction = tilt + "_" + pan

    print("N°", i)
    print("Direction:", direction)
    time.sleep(1)



