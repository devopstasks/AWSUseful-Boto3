import boto3
custom_session=boto3.session.Session(profile_name="dev_root")

s3_re=custom_session.resource(service_name="s3",region_name="us-east-1")
print("Using resource object:")
for each_bucket_info in s3_re.buckets.all():
	print(each_bucket_info)

s3_cli=custom_session.client(service_name="s3",region_name="us-east-1")
print("Using client object:")
for each_bucket_info in s3_cli.list_buckets().get('Buckets'):
	print(each_bucket_info.get('Name'))
