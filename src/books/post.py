import json
import boto3
import os


# import requests
def create_dynamodb_client():
    return boto3.client("dynamodb",region_name=os.environ.get("REGION_NAME"), endpoint_url=os.environ.get("END_POINT"),
                        aws_access_key_id=os.environ.get("ACESS_KEY"), aws_secret_access_key=os.environ.get("SECRET_KEY"))

def create_put_item_input():
    return {
        "TableName": "BookTable",
        "Item": {
            "BookID": {"S": "BookID6"},
            "Author": {"S": "Richard"},
            "Title": {"S": "The Overstory"},
            "Rating": {"N": "5"},
            "Publisher": {"S": "Publisher2"},
            "Language": {"S": "English"},
            "Page_count": {"N": "200"},

        }
    }

def execute_put_item(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.put_item(**input)
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

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
   
   
    if event.get('httpMethod') == 'POST':

        dynamodb_client = create_dynamodb_client()
        put_item_input = create_put_item_input()

        data = execute_put_item(
            dynamodb_client, put_item_input)  # get('Items')
        print(data)
        return {
            "statusCode": 200,
            "body": data

        }

    # Return the response back

