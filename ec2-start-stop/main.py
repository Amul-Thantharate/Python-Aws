import boto3


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')

    for instance in ec2.instances.all():
        state = instance.state['Name']
        if state == 'stopped':
            instance.start()
            print('started your instances: ' + str(instance.id))
            try:
                instance.wait_until_running()
            except:
                print('error')
        else:
            print('No instances to start')
        print('Finished')
