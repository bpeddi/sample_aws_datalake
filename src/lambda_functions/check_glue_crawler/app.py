#!/usr/bin/env python3.8
""" S3 List Lambda function

Lists files under an S3 prefix
"""

# imports added by Lambda layer
# pylint: disable=import-error
# import awswrangler as wr


# pylint: enable=import-error
from os import environ
import boto3
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)



glue = boto3.client("glue")
glue_admin_role_name = environ["glue_admin_role_name"]


def lambda_handler(event, context):
    try:
        print("Write code to check Crawler status and retun SUCESS")


    except Exception as e:
        raise(e)
    event['status'] = "ERROR"
    return event
