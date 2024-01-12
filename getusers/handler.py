import json
from datetime import datetime
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key


def dynamo_table_name(t: str) -> Any:
    """
    FUNCIÓN PARA SELECCIONAR LA TABLA EN DYNAMODB
    """
    _DYNAMODB = boto3.resource("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")
    _table_selected = _DYNAMODB.Table(t)

    return _table_selected


def get_users(event, context):
    """
    FUNCIÓN PARA OBTENER LOS USUARIOS DE LA TABLA USERS
    """

    table_users_get = dynamo_table_name("usersTable")

    response = table_users_get.query(KeyConditionExpression=Key("pk").eq("1"))
    result = response["Items"]

    return {"statusCode": 200, "body": json.dumps(result)}
