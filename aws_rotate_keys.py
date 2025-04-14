#!/usr/bin/env python3
import boto3

iam = boto3.client('iam')
user = iam.get_user()['User']['UserName']
keys = iam.list_access_keys(UserName=user)['AccessKeyMetadata']

if len(keys) >= 2:
    print("Too many keys. Please delete an old one first.")
else:
    new_key = iam.create_access_key(UserName=user)['AccessKey']
    print(f"New Access Key: {new_key['AccessKeyId']}")
    print(f"Secret Access Key: {new_key['SecretAccessKey']}")

    if keys:
        old_key_id = keys[0]['AccessKeyId']
        iam.update_access_key(UserName=user, AccessKeyId=old_key_id, Status='Inactive')
        print(f"Deactivated old key: {old_key_id}")
