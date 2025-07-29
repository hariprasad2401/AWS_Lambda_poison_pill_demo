import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
# table_name = os.environ['DDB_TABLE_NAME']
# table = dynamodb.Table(table_name)
table = dynamodb.Table("dynotbl_1")

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # Get bucket and object key from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download JSON file
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read()
    records = json.loads(content)

    # Insert each record into DynamoDB
    for record in records:
        print("Inserting record:", record)
        table.put_item(Item=record)

    return {
        'statusCode': 200,
        'body': 'Data inserted into DynamoDB'
    }

