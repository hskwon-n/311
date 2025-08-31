import boto3
import json
import csv

AWS_ACCESS_KEY_ID ="ACCESS KEY"
AWS_SECRET_ACCESS_KEY = "SECRET KEY"
AWS_DEFAULT_REGION = input()

#ec2
ec2 = boto3.client('ec2',  aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_DEFAULT_REGION)

Instance = ec2.describe_instances()
aa=[]
paginator = ec2.get_paginator('describe_instances')
page_iterator = paginator.paginate()
for page in page_iterator:
    for reservation in page["Reservations"]:
                    #print(reservation)
                    for instance in reservation["Instances"]:
                        instance_state = instance["State"]["Name"]
                        aa.append([instance['InstanceId'],instance['InstanceType'],instance_state,instance.get('PrivateIpAddress', 'N/A'),instance.get('LaunchTime')])



with open('ec2_report.csv',"w",newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID', 'Instance Type','State','Private IP','LaunchTime'])
    w.writerows(aa)

#s3
s3 = boto3.client('s3',  aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
Bucket = s3.list_buckets()
aa=[]
for bucket in Bucket["Buckets"]:
      region=s3.get_bucket_location(Bucket=bucket["Name"])
      if(region["LocationConstraint"]==AWS_DEFAULT_REGION):
        print(bucket["Name"])
        aa.append(bucket)
      
with open("s3_report.json","w") as f:
    if not aa:
        json.dump({"Buckets":"N/A"},f,indent=2,default=str)
    else:
    
        json.dump({"Buckets":(aa)},f,indent=2,default=str)





