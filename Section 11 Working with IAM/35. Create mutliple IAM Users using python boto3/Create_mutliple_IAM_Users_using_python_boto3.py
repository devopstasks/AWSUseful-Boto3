'''
Take list of iam users in a csv file like

S_NO, IAM_User_Name,Programatic_Access,Console_Access,PolicyARN

1,XYZ, Yes,No,arn:aws:iam::aws:policy/AdministratorAccess

2.pqr,Yes,Yes,arn:aws:iam::aws:policy/AdministratorAccess

3.abc,No,Yes,arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess

'''

import boto3,sys
from pprint import pprint
while True:
  session=boto3.session.Session(profile_name="dev_root")
  iam_re=session.resource(service_name="iam")
  for each in range(701,1100):
   try:
     iam_re.create_user(UserName="ixasisiidemo"+str(each))
     if each==509:
        sys.exit()
   except:
      continue
