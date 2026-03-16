import json


def dynamodb_events(event, context):
    print("DynamoDB event received:")
    print(json.dumps(event, indent=2, default=str))
