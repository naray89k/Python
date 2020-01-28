#!/usr/bin/env python
# coding: utf-8
s = '   hello world  \n'
s.strip()

s.lstrip()

s.rstrip()

t = '-----hello====='
t.strip('-')

t.lstrip('-')

t.strip('-=')

s = '   hello          world     \n'
s = s.strip()
s

s.replace(' ','')

import re
re.sub('\s+', ' ', s)

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:

