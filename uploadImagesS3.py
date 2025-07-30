import boto3
import time
import io
from picamera2 import Picamera2
from time import sleep
import logging
from botocore.exceptions import ClientError

views: dict = {
    "front": {
        "pan": ["left","center","right"],
        "tilt": [0, 90, 180]
    },
    "back": {
        "pan": ["left","center","right"],
        "tilt": [0, 90, 180]
    }
}

s3: boto3.client = boto3.client('s3')

bucket_name: str = 'citric-bucket2'

day: str = time.strftime("%Y-%m-%d", time.localtime())
hour: str = time.strftime("%H:00_%p", time.localtime())
path: str

def upload_fileobj(data, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = path + "image-captured.jpg"

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(data, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def capture_image(picam2: Picamera2):
    
    picam2.start()
    sleep(1)
    data = io.BytesIO()
    picam2.capture_file(data, format='jpeg')
    data.seek(0)
    picam2.stop()
    
    return data

try:
    
    picam0 = Picamera2(0)
    picam1 = Picamera2(1)

    initial_track: int = 1

    while True:
        track = "Track_" + str(initial_track)
        path = day + "/raw/" + hour + "/" + track + "/"
        for view in views:
            for pan in views[view]["pan"]:
                object_name = path + view + "/" + pan
                data = capture_image(picam0 if view == "front" else picam1)
                upload_fileobj(data, bucket_name, object_name)
        initial_track += 1
except KeyboardInterrupt:
    pass
finally:
    print("Subida de archivos terminada")