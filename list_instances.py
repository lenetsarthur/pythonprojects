#!/usr/bin/env python3
import boto3

ec2 = boto3.resource('ec2', aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-2')
for instance in ec2.instances.all():
    print(instance.id, instance.state)
