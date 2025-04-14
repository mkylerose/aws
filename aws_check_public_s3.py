#!/usr/bin/env python3
import boto3

s3 = boto3.client('s3')
buckets = s3.list_buckets()['Buckets']

for bucket in buckets:
    name = bucket['Name']
    acl = s3.get_bucket_acl(Bucket=name)
    for grant in acl['Grants']:
        grantee = grant['Grantee']
        if 'URI' in grantee and 'AllUsers' in grantee['URI']:
            print(f"Bucket {name} is publicly accessible!")
