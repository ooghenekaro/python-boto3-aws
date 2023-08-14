import boto3


# Create a Boto3 EC2 client
ec2 = boto3.client('ec2')

# List of instance IDs you want to terminate
instance_ids = ['i-025afd5a55d21691e', 'i-0de4c890feb359105']

# Terminate instances
response = ec2.terminate_instances(InstanceIds=instance_ids)

# Print response
print("Instance termination initiated:", response)

