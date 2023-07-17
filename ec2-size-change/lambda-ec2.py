try:
    import boto3
    from botocore.exceptions import WaiterError
    print("Loading function")
except Exception as e:
    print("Error: {}".format(e))


def wait_until_instance_stopped(ec2_client, instance_id):
    waiter = ec2_client.get_waiter('instance_stopped')
    try:
        waiter.wait(InstanceIds=[instance_id])
        print("Instance stopped")
    except WaiterError as e:
        print("Error: {}".format(e))


def lambda_handler(event, context):
    instance_id = event['instance_id']
    ec2_client = boto3.client('ec2')
    try:

        ec2_client.stop_instances(InstanceIds=[instance_id])

        wait_until_instance_stopped(ec2_client, instance_id)

        ec2_client.modify_instance_attribute(
            InstanceId=instance_id, InstanceType={'Value': 't2.medium'})

        ec2_client.start_instances(InstanceIds=[instance_id])

        return 'Instance resizing complete.'

    except Exception as e:

        return f'Error resizing instance: {e}'


#  Test event Json:
# {
#   "instance_id": "i-0c1b2a3d4e5f6g7h8"
# }
