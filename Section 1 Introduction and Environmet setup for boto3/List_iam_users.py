import boto3

aws_mag_con_cloud_user=boto3.session.Session(profile_name="cloud_user")

iam_con_re=aws_mag_con_cloud_user.resource(service_name='iam',region_name="us-east-1")
iam_con_cli=aws_mag_con_cloud_user.client(service_name='iam',region_name="us-east-1")


#Listiing iam users with resource object:

for each_user in iam_con_re.users.all():
    print(each_user.name)

#Listing iam users with client object:

for each in iam_con_cli.list_users()['Users']:
   print(each['UserName'])
