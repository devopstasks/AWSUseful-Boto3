'''
Why Copy?
Why would you want to copy an EBS Snapshot from one AWS Region to another?
Use Cases:
Geographic Expansion:
You want to be ableto launch your application in a new Region.
Migration:
You want to be able to migrate your application from one Region to another.
Disaster Recovery:
You want to back up your data and your log files across different  geographical locations  at regular intervals to minimize  data loss and recovery time.

Our requirement is for Disaster recovery
'''

import os,sys
try:
	import boto3
	print("Imported boto3 successfully")
except Exception as e:
	print(e)
	sys.exit(1)

source_region="us-east-1"
dest_region="us-east-2"

session=boto3.session.Session(profile_name="dev_root")
ec2_source_client=session.client(service_name="ec2",region_name=source_region)
sts_client=session.client(service_name="sts",region_name=source_region)
account_id=sts_client.get_caller_identity().get('Account')
bkp_snap=[]
f_bkp={'Name':'tag:backup','Values':['yes']}
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id],Filters=[f_bkp]).get('Snapshots'):
	#print(each_snap.get('SnapshotId'))
	bkp_snap.append(each_snap.get('SnapshotId'))

ec2_dest_client=session.client(service_name="ec2",region_name=dest_region)
for each_source_snapid in bkp_snap:
	print("Taking backup for id of {} into a {}".format(each_source_snapid,dest_region))
	ec2_dest_client.copy_snapshot(
		Description="Disaster Recovery",
		SourceRegion=source_region,
		SourceSnapshotId=each_source_snapid
	)

print("EBS Snapshot copy to destination region is completed")
print("Modifying tags for the snapshots for which backup is completed")

for each_source_snapid in bkp_snap:
	print("Deleting old tags for {}".format(each_source_snapid))
	ec2_source_client.delete_tags(
		Resources=[each_source_snapid],
		Tags=[
			{
				'Key':'backup',
				'Value':'yes'
			}
		]
	)
	print("Creating new tags for {}".format(each_source_snapid))
	ec2_source_client.create_tags(
		Resources=[each_source_snapid],
		Tags=[
			{
				'Key':'backup',
				'Value':'completed'
			}
		]
	)

'''
#Copy the above code into lambda handler to automate
#Comment and update as below line from above script and place the code inside def lambda_handler(event,context):
#session=boto3.session.Session(profile_name="dev_root")
ec2_client=boto3.client(service_name="ec2",region_name="us-east-1")
...
...
return None
'''
