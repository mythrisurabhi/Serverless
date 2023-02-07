import json
import boto3
# client = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000", aws_access_key_id="89z7l8", aws_secret_access_key="w1uezg")


# import requests
def create_dynamodb_client():
    return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://docker.for.mac.localhost:8000/", aws_access_key_id="i0d3go", aws_secret_access_key="7ghp1c")


def create_scan_input():
    return {
        "TableName": "BookTable"
    }


def create_update_item_input():
    return {
        
            "TableName": "BookTable",
            "Key": {
                "BookID": {"S": "BookID2"},
                "Author": {"S": "Martin"}
            },
            "UpdateExpression": "SET #Language = :L",
            "ExpressionAttributeValues": {":L":{"S" : "French"}
        }}


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


def create_delete_item_input():
    return {
        "TableName": "BookTable",
        "Key": {
            "BookID": {"S": "BookID6"},
            "Author": {"S": "corey wilson"}
        }}


def execute_scan(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.scan(**input)
        return response
    except BaseException as error:
        print(error)


def execute_update_item(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.update_item(**input)
        return response
    except BaseException as error:
        print(error)


def execute_put_item(dynamodb_client, input):
    try:
        print('calling dynamodb.')
        response = dynamodb_client.put_item(**input)
        print(response)
        return response
    except BaseException as error:
        print(error)


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

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    if event.get('httpMethod') == 'GET':
        # Create the DynamoDB Client with the region you want
        dynamodb_client = create_dynamodb_client()
    # Create the dictionary containing arguments for get_item call
        scan_input = create_scan_input()
        # path_param = event['pathParameters']
    # Call DynamoDB's get_item API
        data = execute_scan(dynamodb_client= dynamodb_client,input= scan_input).get('Items')
        print(data)
        return {
            "statusCode": 200,
            # "path_param": path_param,
            # "body": json.dumps({"message": data, },
            "body": data

        }
    elif event.get('httpMethod') == 'PUT':
        dynamodb_client = create_dynamodb_client()
        update_item_input = create_update_item_input()

        ##data = execute_update_item(dynamodb_client, update_item_input)
        ##print(data)

        return {
            "statusCode": 200,
            # "body": json.dumps({"message": data})
            "body": "Test"
            



        }
    elif event.get('httpMethod') == 'POST':

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

    elif event.get('httpMethod') == 'DELETE':
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
