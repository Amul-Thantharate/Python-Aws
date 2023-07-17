import json


def lambda_handler(event, context):
    x = event['queryStringParameters']['x']
    y = event['queryStringParameters']['y']
    ops = event['queryStringParameters']['ops']

    print(f"x:{x}, y:{y}, ops:{ops}")

    res_body = {}
    res_body['x'] = int(x)
    res_body['y'] = int(y)
    res_body['ops'] = ops
    res_body['result'] = add(int(x), int(y))

    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = json.dumps(res_body)

    return http_res


def add(x, y):
    return x+y


def mul(x, y):
    return x*y
