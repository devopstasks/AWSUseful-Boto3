'''
Write a Python boto3 script to export IAM User Details into a csv file.

CSV file content is like IAM User Name, User Id, User ARN, User Creation Date,
Attached Policies and Groups associated for IAM Users
'''

import boto3
session=boto3.session.Session(profile_name="dev_root")
'''
iam_re=session.resource(service_name="iam",region_name="us-east-1")
for each_user in iam_re.users.all():
    print "UserName={} UserId={} User ARN={} User Creation Date={}".format(each_user.user_name,each_user.user_id,each_user.arn,each_user.create_date)
'''
iam_cli=session.client(service_name="iam",region_name='us-east-1')

for each_user in iam_cli.list_users()['Users']:
    print each_user['UserName'],each_user['Arn']
