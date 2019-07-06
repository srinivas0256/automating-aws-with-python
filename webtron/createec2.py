import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
 ImageId='ami-035b3c7efe6d061d5',
 MinCount=1,
 MaxCount=2,
 InstanceType='t2.micro')
print instance[0].id
