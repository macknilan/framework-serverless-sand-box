import json
from datetime import datetime

import boto3


def get_users(event, context):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second

    body = {
        "message": f"Go Serverless v3.0! Your function executed successfully! {year}/{month}/{day} {hour}:{minute}:{second}",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
