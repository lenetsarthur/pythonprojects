# !/usr/bin/env python3
import sys
import boto3

ec2 = boto3.resource('ec2', aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-west-2')
for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print(response)
