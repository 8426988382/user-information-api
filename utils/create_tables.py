import boto3

db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000/')
print(db.tables)
db.create_table(
    TableName='educational_info',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
)
