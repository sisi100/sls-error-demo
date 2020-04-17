import json
import urllib.parse
import boto3


def yyyyyy(event, context):
    # URLエンコーディングされているurlをデコードする。
    url = urllib.parse.unquote(event['body']).split('=')[1]

    # dynamoDBに書き込む
    session = boto3.session.Session()
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('yyyy-table-04')

    table.update_item(
        Key={
            'url': url
        },
        UpdateExpression='ADD visitor :incr',
        ExpressionAttributeValues={
            ':incr': 1
        }
    )

    # dynamoDBから訪問数を取得する
    item = table.get_item(Key={'url': url})
    visitor = item['Item']['visitor']

    # Lamda proxy統合を使うため、下記の３キーは必須。
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({"visitor": int(visitor)})
    }
