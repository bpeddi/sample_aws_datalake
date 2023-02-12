#!/usr/bin/env python3.8
""" Incoming Semarchy Workflow Starter

Entry point into the Incoming Semarchy process.
Subscribes to an SQS Queue. Messages in the queue pass an S3 partition.
Starts the Step Function State Machine for the S3 partition
"""
import json
from os import environ
import boto3
import urllib
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    json_event = json.dumps(event)
    logger.info(f'{json_event}')
    resp=""
    if len(event['Records']) >= 1:
        try:
            for record in json.loads(event['Records'][0]['body'])['Records']:
                source_bucket = record['s3']['bucket']['name']
                source_key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
                region = record['awsRegion']
                logger.info(f'{source_bucket}')
                logger.info(f'{source_key}')
                logger.info(f'{region}')
                
                
        except Exception as e:
            logger.info(f'Error Occured {e}')
            return {
                'body': json.loads(json.dumps(e, default=str)),
                'statusCode': 400
            }
