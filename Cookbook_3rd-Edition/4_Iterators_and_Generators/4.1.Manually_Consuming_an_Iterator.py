#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

items = [1,2,3]
it = iter(items)

next(it)

next(it)

next(it)

next(it)



