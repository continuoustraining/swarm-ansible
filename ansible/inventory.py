#!/usr/bin/env python

import json
import boto3
from botocore.config import Config

my_config = Config(region_name = 'us-east-1');

ec2 = ec2 = boto3.resource('ec2' , config=my_config);

custom_master_filter = [{
    'Name':'tag:swarmType', 
    'Values': ['manager']},
    {'Name': 'instance-state-name', 
    'Values': ['running']}];

masters = ec2.instances.filter(Filters=custom_master_filter);

custom_slave_filter = [{
    'Name':'tag:swarmType', 
    'Values': ['worker']},
    {'Name': 'instance-state-name', 
    'Values': ['running']}];

slaves = ec2.instances.filter(Filters=custom_slave_filter);

machines = { 
            'master':  { 'hosts': [] },
            'slave':  { 'hosts': [] },            
        };
i = 0;

for instance in masters :
    machines['master']['hosts'].append(instance.public_ip_address);

    
i = 0;

for instance in slaves :
    machines['slave']['hosts'].append(instance.public_ip_address);
    
print(json.dumps(machines,indent=2));