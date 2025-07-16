import boto3
from botocore.exceptions import ClientError
import logging

def upload_fileobj(data, bucket_name: str, object_name : str = None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = "image-captured.jpg"

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(data, bucket_name, object_name, ExtraArgs={"ContentType": "image/jpeg","ContentDisposition": "inline"})
    except ClientError as e:
        logging.error(e)
        return False
    return True
