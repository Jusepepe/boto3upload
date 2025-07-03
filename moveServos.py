import PanTilt
import cameraController
import upload_fileobj
from typing import List
import time

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
path: str = day + "/raw/" + hour + "/"

bucket_name: str = 'citric-bucket'

upper_sequence = [
    PanTilt.sweep_tilt_up,
    PanTilt.sweep_pan_left,
    PanTilt.sweep_pan_center,
    PanTilt.sweep_pan_right
]

middle_sequence = [
    PanTilt.sweep_tilt_three_quarter_up,
    PanTilt.sweep_pan_center,
    PanTilt.sweep_pan_left
]

lower_sequence = [
    PanTilt.sweep_tilt_quarter_up,
    PanTilt.sweep_pan_center,
    PanTilt.sweep_pan_right
]

lower_sequence = [
    PanTilt.sweep_tilt_quarter_up,
    PanTilt.sweep_pan_left,
    PanTilt.sweep_pan_center,
    PanTilt.sweep_pan_right
]

pan_tilt_1: PanTilt = PanTilt(17, 27)
pan_tilt_2: PanTilt = PanTilt(23, 24)
camera_1: cameraController.Camera = cameraController.Camera(0)
camera_2: cameraController.Camera = cameraController.Camera(1)

#Upper Left
pan_tilt_1.sweep_tilt_up()
pan_tilt_1.sweep_pan_left()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/left")
upload_fileobj(data_2, bucket_name, path + "back/left")

#Upper Center
pan_tilt_1.sweep_pan_center()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/center")
upload_fileobj(data_2, bucket_name, path + "back/center")

#Upper Right
pan_tilt_1.sweep_pan_right()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/right")
upload_fileobj(data_2, bucket_name, path + "back/right")

#Middle Right
pan_tilt_1.sweep_tilt_three_quarter_up()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/right")
upload_fileobj(data_2, bucket_name, path + "back/right")

#Middle Center
pan_tilt_1.sweep_pan_center()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/center")
upload_fileobj(data_2, bucket_name, path + "back/center")

#Middle Left
pan_tilt_1.sweep_pan_left()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/left")
upload_fileobj(data_2, bucket_name, path + "back/left")

#Lower Left
pan_tilt_1.sweep_tilt_quarter_up()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/left")
upload_fileobj(data_2, bucket_name, path + "back/left")

#Lower Center
pan_tilt_1.sweep_pan_center()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/center")
upload_fileobj(data_2, bucket_name, path + "back/center")

#Lower Right
pan_tilt_1.sweep_pan_right()
data_1 = camera_1.capture_image()
data_2 = camera_2.capture_image()
upload_fileobj(data_1, bucket_name, path + "front/right")
upload_fileobj(data_2, bucket_name, path + "back/right")

pan_tilt_1.cleanup()
pan_tilt_2.cleanup()

