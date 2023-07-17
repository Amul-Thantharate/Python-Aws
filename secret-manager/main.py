try:
    import os
    import boto3
    import json

    print("All Modules Loaded ......  Success")
except Exception as e:
    print("Error : {} ".format(e))


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME")


class AwsSecretManager(object):
    __slots__ = ["client", "_session"]

    def __init__(self) -> None:
        self._session = boto3.session.Session()
        self.client = self._session.client(
            service_name="secretsmanager",
            region_name=AWS_REGION_NAME,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

    def get_secrets(self, secret_name=''):
        try:
            if secret_name == '':
                raise Exception("Secret Name cannot be Null ")
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                secret = json.loads(secret)
                for key, value in secret.items():
                    os.environ[key] = value

                return {
                    "status": 200,
                    "error": {},
                    "data": {
                        "message": True
                    }
                }

        except Exception as e:

            return {
                "status": -1,
                "error": {
                    "message": str(e)
                }
            }


print("Start ")
secrets_name = "XXXXX"
secret_manager = AwsSecretManager()
response_secrets = secret_manager.get_secrets(secret_name=secrets_name)
print(

    os.getenv("NAME")

)
