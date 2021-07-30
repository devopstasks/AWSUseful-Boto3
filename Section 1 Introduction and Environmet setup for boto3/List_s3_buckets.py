import boto3

aws_mag_con_cloud_user=boto3.session.Session(profile_name="cloud_user")

s3_con=aws_mag_con_cloud_user.resource(service_name='s3')


#Listiing bucket names:

for each_buck in s3_con.buckets.all():
    print(each_buck.name)
