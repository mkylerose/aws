#!/usr/bin/env python3
import os
import subprocess

local_folder = os.path.expanduser("~/Documents")
bucket = "your-s3-bucket-name"

cmd = ["aws", "s3", "sync", local_folder, f"s3://{bucket}", "--delete"]
result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
print("Sync complete.")
