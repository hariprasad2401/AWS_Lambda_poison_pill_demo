import json

def lambda_handler(event, context):
    print("Received records:", json.dumps(event))

    # Process each record
    for record in event['Records']:
        new_image = record['dynamodb']['NewImage']
        print("Processing record:", new_image)

        # Expect 'value' field to exist
        if 'value' not in new_image:
            # Throw exception -> poison pill will cause entire batch to fail
            raise Exception(f"Malformed record detected: {new_image}")

        print(f"Successfully processed record with id: {new_image['id']['S']}")

    return {
        'statusCode': 200
    }

