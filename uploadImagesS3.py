import boto3
import time
import os

s3: boto3.client = boto3.client('s3')

bucket_name: str = 'citric-bucket'

images_path: str = "D:\\FABIAN\\PLANT_DISEASE\\Imagenes_proyecto\\tndhs2zng4-1\\Images"


date_time: str = time.strftime("%Y-%m-%d %H", time.localtime())

""" for t in range(1,6):
    for filename in os.listdir(images_path)[(t-1)*10:t*10]:
        print("Track", t, "Image", filename) """

for filename in sorted(os.listdir(images_path), key=lambda x: int(x.split(".")[1]) if x.endswith(".jpg") and "aphid" in x else -1 if x.endswith(".jpg") and "aphid" not in x else 0):
    print(filename)

""" for filename in os.listdir(images_path):
    if filename.endswith(".jpg"):
        s3.upload_file(images_path + filename, bucket_name, date_time + "/" + filename) """

print(f"Folder {date_time} created in bucket {bucket_name}")