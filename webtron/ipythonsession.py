# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonautomation')
s3 = session.resource('s3')
for bucket in s3.bucket.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
# to create a new bucket in the region of us-east-1 you should not enter CreateBucketConfiguration={'LocationConstraint': 'us-east-1'} for other regions you have to enter this one.
new_bucket = s3.create_bucket(Bucket='atomatingawssrini-boto3')
