paginator = ec2.get_paginator('describe_instances')
page_iterator = paginator.paginate()
for page in page_iterator:
    for reservation in page["Reservations"]:
                    #print(reservation)
                    for instance in reservation["Instances"]:
                        instance_state = instance["State"]["Name"]
                        aa.append([instance['InstanceId'],instance['InstanceType'],instance_state,instance.get('PrivateIpAddress', 'N/A'),instance.get('LaunchTime')])
                        instance_info = (
                            
                            f"• ID: {instance['InstanceId']}\n"
                            f"• Instance type: {instance['InstanceType']}\n"
                            f"• State: {instance_state}\n"
                            f"• Private IP: {instance.get('PrivateIpAddress', 'N/A')}\n"
                            f"• LaunchTime: {instance.get('LaunchTime')}\n"
                        )
                        print(instance_info)
