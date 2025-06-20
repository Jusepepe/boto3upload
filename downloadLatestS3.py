import boto3

s3 = boto3.client('s3')

bucket_name = 'citric-bucket'

response = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    latest_object = max(response['Contents'], key=lambda x: x['LastModified'])
    print(f"Latest file modified: {latest_object}")
    print(f"Latest object: {latest_object['Key']}")
    
else:
    print("No objects found in the bucket.")
