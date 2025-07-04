import platform
import time
from boto_controller import upload_fileobj

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
path: str = day + "/raw/" + hour + "/"
bucket_name: str = 'citric-bucket'

if platform.system() == "Windows":
    from pan_tilt_mock import PanTiltMock
    from camera_mock import CameraMock
    pan_tilt_1: PanTiltMock = PanTiltMock(17, 27)
    pan_tilt_2: PanTiltMock = PanTiltMock(23, 24)
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
    pan_tilt_1.pan.set_angle(75)
    pan_tilt_2.pan.set_angle(80)
    pan_tilt_1.tilt.set_angle(200)
    pan_tilt_2.tilt.set_angle(145)

reset_servos()
print("Reset")

time.sleep(2)

def capture_image():
    data_1 = camera_1.capture_image()
    data_2 = camera_2.capture_image()
    return data_1, data_2

def upload_images(data_1, data_2, direction):
    upload_fileobj(data_1, bucket_name, path + "front/" + direction)
    upload_fileobj(data_2, bucket_name, path + "back/" + direction)

def move_left():
    pan_tilt_1.pan.set_angle(95)
    pan_tilt_2.pan.set_angle(55)
    pan = "Left"
    return pan

def move_center():
    pan_tilt_1.pan.set_angle(75)
    pan_tilt_2.pan.set_angle(80)
    pan = "Center"
    return pan

def move_right():
    pan_tilt_1.pan.set_angle(35)
    pan_tilt_2.pan.set_angle(110)
    pan = "Right"
    return pan

def move_up():
    pan_tilt_1.tilt.set_angle(200)
    pan_tilt_2.tilt.set_angle(145)
    tilt = "Up"
    return tilt

def move_quarter_up():
    pan_tilt_1.tilt.set_angle(175)
    pan_tilt_2.tilt.set_angle(125)
    tilt = "Quarter Up"
    return tilt
def move_three_quarter_up():
    pan_tilt_1.tilt.set_angle(160)
    pan_tilt_2.tilt.set_angle(100)
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

new_direction = None

for i, sequence in enumerate(complete_sequence):
    tilt, pan = sequence()
    direction = tilt + "_" + pan

    print("N°", i)
    print("Direction:", direction)
    data_1, data_2 = capture_image()
    upload_images(data_1, data_2, direction)

pan_tilt_1.cleanup()
pan_tilt_2.cleanup()