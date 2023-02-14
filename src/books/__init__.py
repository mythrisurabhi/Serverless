import boto3
import os

def create_dynamodb_client():
    if os.environ.get("REGION_NAME") == 'localhost':
        client = boto3.client("dynamodb",region_name=os.environ.get("REGION_NAME"), endpoint_url=os.environ.get("END_POINT"),
                        aws_access_key_id=os.environ.get("ACESS_KEY"), aws_secret_access_key=os.environ.get("SECRET_KEY"))
    else:
        client = boto3.client("dynamodb")
    return client