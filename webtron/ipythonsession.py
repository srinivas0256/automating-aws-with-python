# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonautomation')
s3 = session.resource('s3')
for bucket in s3.bucket.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
    
new_bucket = s3.create_bucket(Bucket='automatingawssrini-boto3',CreatingBucketConfiguration={'LocationConstraint':'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingawssrini-boto3',CreateBucketConfiguration={'LocationConstraint':'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingawssrini-boto3',CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingawssrini-boto3',CreateBucketConfiguration={'LocationConstraint': 'us-east-1})
get_ipython().run_line_magic('history', '')
new_bucket = s3.create_bucket(Bucket='atomatingawssrini-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='atomatingawssrini-boto3')
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('history', '')
import boto3
session = boto3.Session(profile_name = 'pythonautomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client = session.client('ec2')
