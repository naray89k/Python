#!/usr/bin/env python
# coding: utf-8
record = '49586039284958473628492849384928948948392849382'
cost = int(record[20:32]) * float(record[40:48])

print cost

SHARES = record[slice(20,32)]
PRICE = record[slice(40,48)]

cost = int(SHARES) * float(PRICE)

print(cost)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print items[a]
print items[2:4]

items[a] = [10,11]
print items
del items[a]
print items

a = slice(10,50,2)

print a.start
print a.stop
print a.step

#Python 3
s = 'HelloWorld'
a.indices(len(s))

for i in range(*a.indices(len(s))):
    print(s[i])





