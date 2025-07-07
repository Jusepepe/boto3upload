import platform
import time
from boto_controller import upload_fileobj

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
path: str = day + "/raw/" + hour + "/"
bucket_name: str = 'citric-bucket'

is_up = False
is_quarter_up = False

pan1_angles = {"left": 105, "center": 75, "right": 30}
pan2_angles = {"left": 45, "center": 80, "right": 115}
tilt1_angles = {"up": 198, "quarter_up": 175}
tilt2_angles = {"up": 140, "quarter_up": 125}

if platform.system() == "Windows":
    from pan_tilt_mock import PanTiltMock
    from camera_mock import CameraMock
    pan_tilt_1: PanTiltMock = PanTiltMock(17, 27)
    pan_tilt_2: PanTiltMock = PanTiltMock(25, 24)
    camera_1: CameraMock = CameraMock(0)
    camera_2: CameraMock = CameraMock(1)
else:
    from PanTilt import PanTilt
    from camera_controller import Camera
    pan_tilt_1: PanTilt = PanTilt(17, 27)
    pan_tilt_2: PanTilt = PanTilt(23, 24)
    camera_1: Camera = Camera(0)
    camera_2: Camera = Camera(1)

def reset_servos():
    time.sleep(1)
    pan_tilt_1.pan.set_angle(pan1_angles["center"])
    time.sleep(1)
    pan_tilt_2.pan.set_angle(pan2_angles["center"])
    time.sleep(1)
    pan_tilt_1.tilt.set_angle(tilt1_angles["up"])
    time.sleep(1)
    pan_tilt_2.tilt.set_angle(tilt2_angles["up"])
    time.sleep(1)

reset_servos()
print("Reset")

time.sleep(2)

def capture_image():
    data_1 = camera_1.capture_image()
    data_2 = camera_2.capture_image()
    return data_1, data_2

def upload_images(data_1, data_2, direction):
    upload_fileobj(data_1, bucket_name, path + "front/" + direction + ".jpg")
    upload_fileobj(data_2, bucket_name, path + "back/" + direction + ".jpg")

def move_left():
    pan_tilt_1.pan.sweep_to(pan1["left"])
    time.sleep(1)
    pan_tilt_2.pan.sweep_to(pan2["left"])
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
    pan_tilt_2.pan.sweep_to(pan2["right"])
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
    data_1, data_2 = capture_image()
    upload_images(data_1, data_2, direction)
