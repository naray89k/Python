#!/usr/bin/env python
# coding: utf-8
def count(n):
    while True:
        yield n
        n += 1

        
c = count(0)
c[10:20]

# Now using islice()
import itertools

for x in itertools.islice(c, 10, 20):
    print(x)



