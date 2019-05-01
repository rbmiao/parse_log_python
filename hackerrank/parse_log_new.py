#!/usr/bin/python
import re

reader = "hosts_access_log_00.txt" 
y_host = []

with open(reader, 'r') as f:
    for line in f: 
        m = re.split(' ', line)[0]
        y_host.append(m)

counts = dict([x, y_host.count(x)] for x in set(y_host))

for key, value in counts.items():
    print(key, value)