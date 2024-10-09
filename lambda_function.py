
import json
import os
from openai import OpenAI


def get_secret(secret_name, region):
    """Get secret from google cloud api access from environment variables"""
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region)

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    except Exception as e:
        raise e


def set_environment_variables(secret_name):
    # Get the secrets from AWS Secrets Manager
    secrets = get_secret(secret_name)

    # Assuming secrets is a dictionary (from a JSON secret)
    for key, value in secrets.items():
        os.environ[key] = value


def set_environment_variables(secret_name):
    # Get the secrets from AWS Secrets Manager
    secrets = get_secret(secret_name)

    # Assuming secrets is a dictionary (from a JSON secret)
    for key, value in secrets.items():
        os.environ[key] = value


'''messages=[
    {"role": "system", "content": prompt},
    {
        "role": "user",
        "content": "Write a haiku about recursion in programming."
    }
]'''


def create_json_with_openai():
    client = OpenAI()
    prompt = os.environ['OPEN_AI_PROMPT']
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ],

    )


def lambda_handler(event, context):
    # grab secret env info
    secret_name = os.environ['SECRET_NAME']
    # AWS Lambda provides this automatically
    region = os.environ['AWS_REGION']
    # Get Open AI Credentials from Secrets Manager
    credentials_dict = get_secret(secret_name, region)

    print(credentials_dict)

    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
