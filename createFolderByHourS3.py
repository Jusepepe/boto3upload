import boto3
import time
import os

s3: boto3.client = boto3.client('s3')

bucket_name: str = 'citric-bucket2'

images_path: str = "./"


date_time: str = time.strftime("%Y-%m-%d %H:00 %p", time.localtime())

""" for filename in os.listdir(images_path):
    if filename.endswith(".jpg"):
        s3.put_object(Bucket=bucket_name, Key=date_time + "/" + filename, object_name=date_time + "/" + filename) """

#s3.put_object(Bucket=bucket_name, Key=date_time + "/")

print(f"Folder {date_time} created in bucket {bucket_name}")
