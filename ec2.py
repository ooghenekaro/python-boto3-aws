import boto3


# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Create an EC2 instance
response = ec2.run_instances(
    ImageId='ami-0eb260c4d5475b901',          # Change to the desired AMI ID
    InstanceType='t2.micro',   # Change to the desired instance type
    MinCount=1,
    MaxCount=2,
)

# Extract the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance ID: {instance_id}")

# Wait for the instance to be in the 'running' state
waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

# Describe the instance to get its public IP address
response = ec2.describe_instances(InstanceIds=[instance_id])
public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
print(f"Public IP: {public_ip}")

