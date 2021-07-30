'''
Mail Alert: get AWS EC2 instances status when it stopped

Step-1
Lambda Function --> IAM Roles(EC2,IAM)

Step-2
Create a lambda with boto3 of python
MailAlertForProdServers

lambda_function
'''

import json
import boto3

def lambda_handler(event,context):
	#Thecommented lines are not required if scheduled through cloudwatch
	#ec2_con=boto3.resource("ec2","us-east-1")
	sns_client=boto3.client("sns","us-east-1")
	#my_ins=ec2_con.Instance("i-020029a18ce55706")
	#print my_ins.state['Name']

	#The SNS topic is configured with some email address, copy the arn from that topic and use in below
	#sns_client.publish(TargetArn="arn:aws:sns:us-east-1:967636435446:Status_of_Ec2",Message=my_ins.state['Name'])
	sns_client.publish(TargetArn="arn:aws:sns:us-east-1:967636435446:Status_of_Ec2",Message="Now instance is in stopped Status")


	return "Success"

'''
Step-3
Configure Cloudwatch event
Create Rule -> Event Pattern -> Service Name=EC2 , Event Type=EC2 Instance State-change Notification ->
Specific state="Stopped"
Specific instance ids=i-020029a18ce55706
Add the target to lambda function
Create the rule name as "MailAlertForProdServers"


Scenario: You are having one Security Group and for that security group incase if the inbound got changed other than your required port
at that time automatically I want to send mail alert. This is used for compliance purpose.
'''
