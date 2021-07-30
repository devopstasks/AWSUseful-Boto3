'''
Paginators:
Paginators play a role when weuse boto3 to query AWS resource.
Like get all EC2 instances, IAM users, buckets, objects etc.
For query, API calls are made to AWS through boto3.
Generally each API call will return 50 or 100 results.
Note: S3 will return upto 1000 results.
Actually each API call return a page and each page consist of information of 50 or 100 results(Except S3 objects)

Example: To get all IAM users info using boto3 client method
Default API Client call will giveone page and that page consist of only 100 users info the what about remaining IAM users?
Collect all pages to get info of all IAM users.
If you are trying to retrieve more than one "page" of results you will need to use a paginator to issue multiple API requests on your behalf.
Boto3 provides Paginators to automatically issue multiple API requests to retrieve all the pages(from page all results.)
Paginators are straightforward to use.
But not all Boto3 services provide paginator support.For those services you will need to write your own paginator in Python.

How to use Paginators?
Step1: Create a paginator
Step2: Paginate through created paginator to get pages one by one
'''

import boto3

'''
session=boto3.session.Session(profile_name="dev_root")
iam_re=session.resource("iam")
cnt=1
for each_user in iam_re.users.all():
	print cnt,each_user.user_name
	cnt=cnt+1

cnt=1
iam_cli=session.client("iam")
for each_user in iam_cli.list_users()['Users']:
	print cnt, each_user['UserName']
	cnt=cnt+1
'''

'''
cnt=1
iam_cli=session.client("iam")
paginator=iam_cli.get_paginator('list_users')
for each_page in paginator.paginate():
	for each_user in each_page['Users']
		print cnt,each_user['UserName']
		cnt=cnt+1
'''

iam_cli=session.client("ec2")
paginatro=iam_cli.get_paginator('describe_instances')
for each_page in paginatro.paginate():
	print each_page

'''
Till now below are covered
resource
client
waiter
paginator
'''
