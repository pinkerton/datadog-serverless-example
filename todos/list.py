import json
import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import boto3
from datadog import datadog_lambda_wrapper, lambda_metric

from todos import decimalencoder

dynamodb = boto3.resource('dynamodb')

@datadog_lambda_wrapper
def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
