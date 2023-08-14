import boto3

client =boto3.client ('ec2')

response = client.monitor_instances(
    InstanceIds=[
        'i-025afd5a55d21691e',
    ],
    DryRun=False
)

print(response)
