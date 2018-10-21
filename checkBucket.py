#!/usr/bin/env python2

import dns.resolver
import argparse

parser = argparse.ArgumentParser(description='Search if S3 bucket Exists.')
parser.add_argument('wordlist',help="S3 bucket wordlist")

args = parser.parse_args()

file=open(args.wordlist,"r")

for bucket in file:
    S3bucket=bucket.strip()+'.s3.amazonaws.com'.strip()
    answers = dns.resolver.query(S3bucket, 'CNAME')
    for rdata in answers:
        if "s3-directional" not in str(rdata.target): 
            print S3bucket+' bucket Exists! cname target address:', rdata.target
file.close()
