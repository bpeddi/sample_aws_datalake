#!/usr/bin/env python3.8
""" S3 List Lambda function

Lists files under an S3 prefix
"""
import awswrangler as wr
# imports added by Lambda layer
# pylint: disable=import-error
# import awswrangler as wr


# pylint: enable=import-error

import boto3

glue = boto3.client("glue")

def create_glue_crawler(crawler_name, database_name, s3_path):
    response = glue.create_crawler(
        Name=crawler_name,
        Role="AWSGlueServiceRoleDefault",
        DatabaseName=database_name,
        Description="Glue Crawler for " + database_name,
        Targets={
            "S3Targets": [
                {
                    "Path": s3_path
                }
            ]
        },
        Schedule="cron(0 0 * * ? *)",
        Classifiers=[
            "parquet",
            "json"
        ]
    )
    print("Crawler created with name: " + crawler_name)



def lambda_handler(event, context):
    try:
        status = wr.catalog.create_database(
                    name='legislators'
                )
        # status= wr.catalog.create_json_table(
        #             database='default',
        #             table='persons_json',
        #             path='s3://balaaws-s3-ingest-321/input_data/persons.json',

        #         )
        create_glue_crawler("my_crawler", "legislators", "s3://balaaws-s3-ingest-321/input_data/persons.json")
    except Exception as e:
        raise(e)


    return None
