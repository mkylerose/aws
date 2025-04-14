#!/usr/bin/env python3
import boto3

ec2 = boto3.client('ec2')
regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]

for region in regions:
    print(f"Region: {region}")
    ec2_regional = boto3.client('ec2', region_name=region)
    instances = ec2_regional.describe_instances()
    for res in instances['Reservations']:
        for inst in res['Instances']:
            name = next((t['Value'] for t in inst.get('Tags', []) if t['Key'] == 'Name'), 'N/A')
            print(f"  Instance ID: {inst['InstanceId']}, Name: {name}, State: {inst['State']['Name']}")
