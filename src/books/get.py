import json
import boto3
import os
from . import create_dynamodb_client 


def create_scan_input():
    return {
        "TableName": "BookTable"
    }


def execute_scan(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.scan(**input)
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

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    
    
    
    
        # Create the DynamoDB Client with the region you want
        
    dynamodb_client = create_dynamodb_client()
    # Create the dictionary containing arguments for get_item call
    scan_input = create_scan_input()

    # Call DynamoDB's get_item API
    data = execute_scan(dynamodb_client=dynamodb_client,
                        input=scan_input).get('Items')
    
    return {
        "statusCode": 200,
        # "path_param": path_param,
        # "body": json.dumps({"message": data, },
        "body": json.dumps(data)

    }
