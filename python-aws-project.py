#to connect aws with python, use boto3 library of aws
import boto3

s3= boto3.resource('s3')
print(s3.buckets.all())
for bucket in s3.buckets.all():
    print(bucket)

