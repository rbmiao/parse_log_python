#!/usr/bin/python
import sys, itertools
import re
import codecs
from collections import Counter
import collections

 
reader    = "/home/vagrant/web/hackerrank/hosts_access_log_00.txt"
y_host    = []
y_time    = []
y_request = []
y_status  = []
y_size    = []

## Regex for the input Apache log file
parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'\S+',                             # indent %l (unused)
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')


with codecs.open(reader, encoding='utf-8') as f:
    for line in f: 
        m = pattern.match(line)
        res = m.groupdict()
        y_host.append(res["host"])
        y_time.append(res["time"])
        y_request.append(res["request"])
        y_status.append(res["status"])
        y_size.append(res["size"])



for count, elem in sorted(((y_host.count(e), e) for e in set(y_host)), reverse=True):
    print(('{} {}').format(elem, count))
