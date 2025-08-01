import boto3
import logging
from botocore.exceptions import ClientError
import os
import sys
import threading
from picamera2 import Picamera2
import io
from time import sleep

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))/1000
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount/1000
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s kB  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = "images/" + os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, Callback = ProgressPercentage(file_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_fileobj(data, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = "images/image-captured.jpg"

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(data, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def capture_image():
    
    picam2.start()
    sleep(1)
    data = io.BytesIO()
    picam2.capture_file(data, format='jpeg')
    data.seek(0)
    picam2.stop()
    
    return data

try:
    
    picam2 = Picamera2()
    while True:
        file_name = input("Escribir el nombre del archivo a subir(o 't' para tomar foto:)")
        print(file_name)
        
        if file_name.lower() == "t":
            data = capture_image()
            upload_fileobj(data, "citric-bucket")
        else:
            upload_file(file_name, "citric-bucket")

except KeyboardInterrupt:
    pass
finally:
    print("Subida de archivos terminada")

