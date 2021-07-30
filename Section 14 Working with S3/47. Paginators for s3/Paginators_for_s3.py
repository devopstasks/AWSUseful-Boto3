#List all objects of a bucket

import boto3
session=boto3.session.Session(profile_name="dev_root")
'''
s3_re=session.resource(service_name="s3",region_name="us-east-1")
bucket_name="dowithpythonapril"
bucket_object=s3_re.Bucket(bucket_name)
cnt=1
for each_obj in bucket_object.objects.all():
	print(cnt,each_obj.key)
	cnt=cnt+1
'''

'''
s3_cli=session.client(service_name="s3",region_name="us-east-1")
bucket_name="dowithpythonapril"
cnt+1
for each_object in s3_cli.list_objects(Bucket=bucket_name)['Contents']:
	print(cnt,each_object['Key'])
	cnt=cnt+1
'''

cnt=1
s3_cli=session.client(service_name="s3",region_name="us-east-1")
bucket_name="dowithpythonapril"
paginator=s3_cli.get_paginator('list_objects')
for each_page in paginator.paginate(Bucket=bucket_name):
	for each_object in each_page['Contents']:
		print(cnt,each_object['Key'])
		cnt=cnt+1
