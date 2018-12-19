#!/usr/bin/env python3
import boto3

ec2 = boto3.resource('ec2', aws_access_key_id='AKIAJMFYUSHZ7VJR2WWA',
    aws_secret_access_key='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',
    region_name='us-east-2')
for instance in ec2.instances.all():
    print(instance.id, instance.state)