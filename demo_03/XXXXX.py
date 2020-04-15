import json
import boto3
import datetime


def yyyyyy(event, context):

    # キューのbody取り出す
    queue = json.loads(event['Records'][0]['body'])
    print(queue)

    # dynamoDBに書き込む
    session = boto3.session.Session()
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('yyyy-dynamo')
    response = table.put_item(
        Item={
            "pk": str(datetime.datetime.now()),
            'queue': str(queue)
        }
    )
    if not response['ResponseMetadata']['HTTPStatusCode'] is 200:
        # 失敗処理
        print(response)
    else:
        # 成功処理
        print('Successed')

    return True
