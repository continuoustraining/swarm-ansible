#!/usr/bin/python36

import json
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1');

ec2 = boto3.resource('ec2' , config=my_config);

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
            'main': { 'hosts': [] },
            'master':  { 'hosts': [], 'vars': {} },
            'slave':  { 'hosts': [], 'vars': {}  }         
        };

managers = list(masters);
main = list(masters).pop(0);
machines['main']['hosts'].append(main.public_ip_address);

machines['master']['vars'] = {'mainAddr': main.public_ip_address};
machines['slave']['vars'] = {'mainAddr': main.public_ip_address};

for instance in managers :
    machines['master']['hosts'].append(instance.public_ip_address);


for instance in slaves :
    machines['slave']['hosts'].append(instance.public_ip_address);
    
print(json.dumps(machines,indent=2));