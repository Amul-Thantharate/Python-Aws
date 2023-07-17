try:
    import re
    import os
    import json
    import boto3
    import datetime
    import uuid
    from datetime import datetime
    import json
    from faker import Faker
    import random
    import faker

except Exception as e:

    print("Error : {} ".format(e))


acess_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_REGION')


def main():
    for i in range(1, 20):
        faker = Faker()
        json_data = {
            "name": faker.name(),
            "phone_numbers": faker.phone_number(),
            "city": faker.city(),
            "address": faker.address(),
            "date": str(faker.date()),
            "customer_id": str(random.randint(1, 5))
        }
        print(json_data)
        client = boto3.client(
            "firehose",
            aws_access_key_id=acess_key,
            aws_secret_access_key=secret_key,
            region_name=aws_region
        )
        response = client.put_record(
            DeliveryStreamName="Enter your stream name",
            Record={
                "Data": json.dumps(json_data)
            }
        )
        print(response)


main()
