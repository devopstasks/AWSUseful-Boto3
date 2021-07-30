'''
Everyday
Start EC2 Instances at 8am Mon-Fri
Stop EC2 Instances at 5pm Mon-Fri

Step-1: Create a Role for Lambda Function

Role name: LambdaRoleToWorkWithEC2
Role description: Allows Lambda function to call AWS services on your behalf.
Policies: AWSEC2FullAccess

Step-2: Write a Lambda Function using boto3 of python

AutoStartTestEC2Instances_8am
AutoStopTestEC2Instances_5pm

lambda_function
'''

import boto3

def lambda_handler(event,context):
	ec2_con_re=boto3.resource(service_name="ec2",region_name="us-east-1")
	test_env_filter={"Name":"tag:Env","Values":["Test"]}
    for each_in in ec2_con_re.instances.filter(Filters=[test_env_filter]):
		each_in.start()

	return "Success"

'''
Step-3: Schedule the job

Goto CloudWatch -> Rules -> Create Rule-> Schedule -> Cron Expression (0 8 ? * MON-FRI *)

Add Target -> Select the Lambda function "AutoStartTestEC2Instances_8am"

Rule Definition -> Name="AutoStartTestEC2Instances_8am" -> Create Rule


AutoStopTestEC2Instances_5pm

lambda_function
'''

import boto3

def lambda_handler(event,context):
	ec2_con_re=boto3.resource(service_name="ec2",region_name="us-east-1")
	test_env_filter={"Name":"tag:Env","Values":["Test"]}
    for each_in in ec2_con_re.instances.filter(Filters=[test_env_filter]):
		each_in.stop()

	return "Success"
