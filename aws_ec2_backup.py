#!/usr/bin/env python3
import boto3

ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    name = next((t['Value'] for t in instance.tags if t['Key'] == 'Name'), instance.id)
    ami = instance.create_image(Name=f"Backup-{name}", NoReboot=True)
    print(f"Created AMI for {name}: {ami.id}")
