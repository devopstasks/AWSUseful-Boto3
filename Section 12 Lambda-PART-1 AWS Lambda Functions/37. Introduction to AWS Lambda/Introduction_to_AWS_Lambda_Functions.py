'''
AWS Lambda is a serverless computing platform that allows engineers to create a small function
, configure the function in AWS console, and have the code executed without the need to provision servers- paying only for the resources used during execution

Simply, it is like an editor(vim, Pycharm, Sublimetext, atom) with some extra features.

It supports to run different languages like- python, go, java, Node.js etc.

It is installed or running on Amazon Linux server and we can access /tmp using Lambda function


	A Lambda function has few requirements.
	The first requirement you need to satisfy is to provide a handler.
•	The handler is the entry point for the Lambda
•	A Lambda function accepts JSON-formatted input and usually return the same.

	The second requirement is that you will need to specify the runtime environment for the Lambda. The runtime will usually correlate directly with the language you selected to write your function.

	The final requirement is a trigger
•	Manual trigger or run by us
•	You can configure a Lambda invocation in response to an event, such as a new file uploadded to S3, a change in the DynamoDB table, or a similar AWS event. You can also configure Lambda to respond to requests to AWS API Gateway or based on a timer triggered by AWS Cloudwatch

How AWS Lambda function executes the code for AWS services
Two ways:
	Use Programmatic Access keys
	Create a AWS IAM Role and attach the role to AWS Lambda

DemoPythonLambdaFunction
'''

import boto3

def lambda_handler(event, context):
	s3_con=boto3.resource("s3","us-east-1")
	for each_bu in s3_con.buckets.all():
	  print each_bu.name
