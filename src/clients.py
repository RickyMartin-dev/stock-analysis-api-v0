import os, json, boto3

_lambda = boto3.client('lambda')
INFER_FN = os.environ['INFERENCE_FUNCTION_NAME'] # use alias e.g., my-fn:prod

def invoke_model(ticker: str):
    payload = {"ticker": ticker}
    resp = _lambda.invoke(FunctionName=INFER_FN,
    InvocationType='RequestResponse',
    Payload=json.dumps({"body": json.dumps(payload) }))
    body = json.loads(resp['Payload'].read().decode('utf-8'))
    if body.get('statusCode') != 200:
        raise RuntimeError(body.get('body'))
    return json.loads(body['body'])