#!/usr/bin/env python3

import argparse
import boto3
import datetime


parser = argparse.ArgumentParser()
parser.add_argument('--days', type=int, default=30)
args = parser.parse_args()


now = datetime.datetime.utcnow()
start = (now - datetime.timedelta(days=args.days)).strftime('%Y-%m-%d')
end = now.strftime('%Y-%m-%d')

cd = boto3.client('ce', aws_access_key_id='',
    aws_secret_access_key='',
)

results = []

token = None
while True:
    if token:
        kwargs = {'NextPageToken': token}
    else:
        kwargs = {}
    data = cd.get_cost_and_usage(TimePeriod={'Start': start, 'End':  end},
                                 Granularity='DAILY',
                                 Metrics=['UnblendedCost'],
                                 GroupBy=[{'Type': 'DIMENSION', 'Key': 'LINKED_ACCOUNT'},
                                          {'Type': 'DIMENSION', 'Key': 'SERVICE'}], **kwargs)
    results += data['ResultsByTime']
    token = data.get('NextPageToken')
    if not token:
        break

#import pickle
#pickle.dump(data,open('data.p','wb'))
print('\t'.join(['TimePeriod', ' Amount', '\t', ' Unit', ' LinkedAccount', 'Service']))
for result_by_time in results:
    for group in result_by_time['Groups']:
        amount = group['Metrics']['UnblendedCost']['Amount']
        unit = group['Metrics']['UnblendedCost']['Unit']
        print(result_by_time['TimePeriod']['Start'], '\t', amount, '\t', unit, '\t', '\t'.join(group['Keys']), '\t')
