import boto3
from botocore.client import Config


s3_client = boto3.client('s3',region_name='ap-south-1',aws_access_key_id = 'AKIA4DLKI7MR6JYOID5U',aws_secret_access_key='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',config=Config(signature_version='s3v4'))

s3_client.upload_file("/home/mayur/Downloads/passport_mayur.pdf", "awss3outputrml", "passport_mayur.pdf")

