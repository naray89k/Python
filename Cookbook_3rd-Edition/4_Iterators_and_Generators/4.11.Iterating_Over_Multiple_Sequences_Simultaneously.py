#!/usr/bin/env python
# coding: utf-8
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x,y)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip(a,b):
    print(i)

#Python 3
from itertools import zip_longest

for i in zip_longest(a,b):
    print(i)
    

for i in zip_longest(a, b, fillvalue=0):
    print(i)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']

for i in zip(a, b, c):
    print(i)

zip(a,b)



