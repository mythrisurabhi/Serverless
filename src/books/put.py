import json
import boto3
# client = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000", aws_access_key_id="89z7l8", aws_secret_access_key="w1uezg")


# import requests
def create_dynamodb_client():
    return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://docker.for.mac.localhost:8000/", aws_access_key_id="i0d3go", aws_secret_access_key="7ghp1c")


def create_update_item_input():
    return {
        "TableName": "BookTable",
        "Key": {
            "BookID": {"S": "BookID3"},
            "Author": {"S": "Steve Mcconnell"}
        },
        "UpdateExpression": "SET #language = :language",
        "ExpressionAttributeNames":
        {
            "#language": "Language"
        },
        "ExpressionAttributeValues":
        {
            ":language":
            {
                "S": "Telugu-Lambda"
            }
        },
        "ReturnValues": "UPDATED_NEW",
    }


def execute_update_item(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.update_item(**input)
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

    if event.get('httpMethod') == 'PUT':
        dynamodb_client = create_dynamodb_client()
        update_item_input = create_update_item_input()

        data = execute_update_item(dynamodb_client, update_item_input)
        # print(data)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": data})
        }
