import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(Filters=[
    {
        'Name': 'tag:Name',
        'Values': ['Karo-Instance']
    }
])

# Extract instance IDs
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])
        tags = instance.get('Tags', [])
        
        print(f"Instance ID: {instance_ids}")
        for tag in tags:
            print(f"Tag Key: {tag['Key']}, Tag Value: {tag['Value']}")
        
        print()  # Empty line to separate instances

# Terminate instances
ec2.terminate_instances(InstanceIds=instance_ids)

