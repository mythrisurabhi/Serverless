import json
import boto3
import os



# import requests
def create_dynamodb_client():
    if os.environ.get("REGION_NAME") == 'localhost':
        client = boto3.client("dynamodb",region_name=os.environ.get("REGION_NAME"), endpoint_url=os.environ.get("END_POINT"),
                        aws_access_key_id=os.environ.get("ACESS_KEY"), aws_secret_access_key=os.environ.get("SECRET_KEY"))
    else:
        client = boto3.client("dynamodb",region_name=os.environ.get("REGION_NAME"))
    return client


def create_delete_item_input():
    return {
        "TableName": "BookTable",
        "Key": {
            "BookID": {"S": "BookID5"},
            "Author": {"S": "John Sonmez"}
        }}
def execute_delete_item(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.delete_item(**input)
        print(response)
        return response
    except BaseException as error:
        print(error)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        #api-gateway-simple-proxy-for-lambda-input-format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    
    

    
    dynamodb_client = create_dynamodb_client()
    delete_item_input = create_delete_item_input()
    data = execute_delete_item(dynamodb_client, delete_item_input)  # get('Items')
    return {
            "statusCode": 200,
            "body": data,
            
        }
