"""
AWS S3 Controller

This module provides functionality to interact with AWS S3 for file uploads.
It handles the upload of files to specified S3 buckets with proper content types.
"""

import logging
from typing import BinaryIO, Optional
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def upload_fileobj(
    file_obj: BinaryIO,
    bucket_name: str,
    object_name: Optional[str] = None,
    content_type: str = "image/png",
    content_disposition: str = "inline"
) -> bool:
    """Upload a file-like object to an S3 bucket.

    Args:
        file_obj: A file-like object to upload.
        bucket_name: Name of the S3 bucket.
        object_name: S3 object name. If not specified, 'image-captured.png' is used.
        content_type: MIME type of the file. Defaults to 'image/png'.
        content_disposition: Specifies presentational information. Defaults to 'inline'.

    Returns:
        bool: True if file was uploaded successfully, False otherwise.
    """
    if object_name is None:
        object_name = "image-captured.png"

    try:
        s3_client.upload_fileobj(
            file_obj,
            bucket_name,
            object_name,
            ExtraArgs={
                "ContentType": content_type,
                "ContentDisposition": content_disposition
            }
        )
        return True
    except ClientError as e:
        logging.error("Error uploading file to S3: %s", e)
        return False
