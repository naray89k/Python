#!/usr/bin/env python
# coding: utf-8
mylist = [1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n>0])
print([n for n in mylist if n<0])

pos = (n for n in mylist if n > 0)
print(pos)
for i in pos:
    print i

neg = (n for n in mylist if n < 0)
print(neg)
for i in neg:
    print i

values = ['1','2','-3','-','4','N/A','5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))
print(ivals)

values = ['1','2','-3','-','4','N/A','5']
integers = []
for i in values:
    try:
        if type(int(i)) == int:
            integers.append(str(i))
    except ValueError:
        pass
integers

mylist = [1,4,-5,10,-7,2,3,-1]
import math

[math.sqrt(n) for n in mylist if n>0]

clip_neg = [n if n>0 else 0 for n in mylist]

clip_neg

clip_pos = [n if n<0 else 0 for n in mylist]

clip_pos

addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n>5 for n in counts]
more5

list(compress(addresses,more5))



