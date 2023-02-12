import sys
from awsglue.transforms import Join
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())
persons = glueContext.create_dynamic_frame.from_catalog(database="legislators", table_name="persons_json")
print("Count: ", persons.count())
persons.printSchema()

glueContext.write_dynamic_frame.from_options(frame = l_history,
          connection_type = "s3",
          connection_options = {"path": "s3://balaaws-s3-ingest-321/output-dir/persons_parquet"},
          format = "parquet")