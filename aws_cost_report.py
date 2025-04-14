#!/usr/bin/env python3
import boto3
from datetime import date, timedelta

client = boto3.client('ce')
end = date.today().replace(day=1)
start = (end - timedelta(days=1)).replace(day=1)

response = client.get_cost_and_usage(
    TimePeriod={'Start': str(start), 'End': str(end)},
    Granularity='MONTHLY',
    Metrics=['UnblendedCost'],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
)

for group in response['ResultsByTime'][0]['Groups']:
    service = group['Keys'][0]
    amount = group['Metrics']['UnblendedCost']['Amount']
    print(f"{service}: ${float(amount):.2f}")
