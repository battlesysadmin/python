#!/usr/bin/env python

import boto.ec2
import hashlib

try:
     conn = boto.ec2.connect_to_region ("us-west-2")
     current_sgs = conn.get_all_security_groups()
except boto.exception.BotoServerError, e:
     log.error(e.error_message)
conn.close()

for sg in current_sgs:
     print "="*72
     print "id:\t\t", sg.id
     print "name:\t\t", sg.name
     print "vpc:\t\t", sg.vpc_id
     print "instance:\t", sg.instances()
     for rule in sg.rules:
         print "\t",rule.grants,"-> [instance]:",rule.from_port,"-",rule.ip_protocol
     print "="*72
     print " "
