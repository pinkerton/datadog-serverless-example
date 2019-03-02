import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import boto3
from datadog import datadog_lambda_wrapper, lambda_metric

dynamodb = boto3.resource('dynamodb')

@datadog_lambda_wrapper
def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
