#!/usr/bin/env python3
import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client('ec2')
cutoff = datetime.now(timezone.utc) - timedelta(days=30)

snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
for snap in snapshots:
    if snap['StartTime'] < cutoff:
        print(f"Deleting snapshot {snap['SnapshotId']} from {snap['StartTime']}")
        ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
