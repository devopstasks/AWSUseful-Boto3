'''
Automated EBS Snapshots using AWS Lambda & Cloudwatch

Steps:
Write a code to list all EBS Volumes based on requirement
Extend Script to take snapshots
Finally we will implement code to take snapshpts with lambda using cloudwatch trigger or we will schedule a job with lambda and cloudwatch.

Steps-1
Write a code to list all EBS Volumes based on requirement

#Note: This code works for a single specified region
'''
import boto3
import pprint

session=boto3.session.Session(profile_name="dev_root")
ec2_client=session.client(service_name="ec2",region_name="us-east-1")
#pprint(ec2_client.describe_volumes()['Volumes'])
list_of_volids=[]
f_prod_bkp={'Name':'tag:Prod','Values':['backup','Backup']}
#The below commented code works perfectly, if no. of volumes are less than 50. If more than 50 volumes, we have to use paginators
#for each_vol in ec2_client.describe_volumes()['Volumes']:
#	list_of_volids.append(each_vol['volumeId'])

paginator=ec2_client.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[f_prod_bkp]):
	#pprint(each_page['Volumes'])
	for each_vol in each_page['Volumes']:
		list_of_volids.append(each_vol['VolumeId'])

print "The list of volids are: ".list_of_volids

snapids=[]
for each_volid in list_of_volids:
	print "Taking snap of {}".format(each_volid)
	res=ec2_client.create_snapshot(
					Description="Taking snap with Lambda and CW",
					VolumeId=each_volid,
					TagSpecifications=[
						{
							'ResourceType':'snapshot',
							'Tags': [
								{
									'Key': 'Delete-on',
									'Value': '90'
								}
							]


						}

					]
		)

	#print(res.get('SnapshotId'))
	snapids.append(res.get('SnapshotId'))
	print "The snap ids are:",snapids

	waiter=ec2_client.get_waiter('snapshot_completed')
	waiter.wait(SnapshotIds=snapids)

	print "Successfully completed snaps for the volumes of {}".format(list_of_volids)

	return "Success"

'''
Steps-2
Lambda function name = AutomateSnapsForEBSVolumes

#Comment andupdate as below line from above script and place the code inside def lambda_handler(event,context):
#session=boto3.session.Session(profile_name="dev_root")
ec2_client=boto3.client(service_name="ec2",region_name="us-east-1")
...
...
return None


Step-3
Schedule a job using Cloudwatch event for automate the snapshots
'''
