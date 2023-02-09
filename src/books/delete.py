import json
import boto3
# client = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000", aws_access_key_id="89z7l8", aws_secret_access_key="w1uezg")


# import requests
def create_dynamodb_client():
    return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://docker.for.mac.localhost:8000/", aws_access_key_id="i0d3go", aws_secret_access_key="7ghp1c")


def create_delete_item_input():
    return {
        "TableName": "BookTable",
        "Key": {
            "BookID": {"S": "BookID6"},
            "Author": {"S": "corey wilson"}
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

    
    

    if event.get('httpMethod') == 'DELETE':
        dynamodb_client = create_dynamodb_client()
        delete_item_input = create_delete_item_input()
        data = execute_delete_item(
            dynamodb_client, delete_item_input)  # get('Items')
        print(data)
        return {
            "statusCode": 200,
            "body": data,
            "message": "delete request recieved"
        }
