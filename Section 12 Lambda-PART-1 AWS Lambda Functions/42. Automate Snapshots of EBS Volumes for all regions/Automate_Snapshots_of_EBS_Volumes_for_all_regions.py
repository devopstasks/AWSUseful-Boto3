import boto3

session=boto3.session.Session(profile_name="dev_root")
ec2_client=session.client(service_name="ec2",region_name="us-east-1")

all_regions=[]
for each_region in ec2_client.describe_regions()['Regions']:
	#print(each_region.get('RegionName'))
	all_regions.append(each_region.get('RegionName'))

for each_region in all_regions:
	print("Working on {}".format(each_region))
	ec2_client=session.client(service_name="ec2",region_name=each_region)

	list_of_volids=[]
	f_prod_bkp={'Name':'tag:Prod','Values':['backup','Backup']}

	paginator=ec2_client.get_paginator('describe_volumes')
	for each_page in paginator.paginate(Filters=[f_prod_bkp]):
		#pprint(each_page['Volumes'])
		for each_vol in each_page['Volumes']:
			list_of_volids.append(each_vol['VolumeId'])

	print("The list of volids are: ",list_of_volids)
	if bool(list_of_volids)==False:
		continue

	snapids=[]
	for each_volid in list_of_volids:
		print("Taking snap of {}".format(each_volid))
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
		print("The snap ids are:",snapids)

		waiter=ec2_client.get_waiter('snapshot_completed')
		waiter.wait(SnapshotIds=snapids)

		print("Successfully completed snaps for the volumes of {}".format(list_of_volids))

'''
#Copy the above code into lambda handler to automate
#Comment and update as below line from above script and place the code inside def lambda_handler(event,context):
#session=boto3.session.Session(profile_name="dev_root")
ec2_client=boto3.client(service_name="ec2",region_name="us-east-1")
...
...
return None

#The only challenge in automating this is based on the number of volumes, we have to calculate the time taken for taking snapshots and set the
timeout in Lambda function.
'''
