#!/usr/bin/env python
# coding: utf-8
print('ACME', 50, 91.5)

# Python 3
print('ACME', 50, 91.5, sep=',')

# Python 2
from __future__ import print_function
print('ACME', 50, 91.5, sep=',')

#Python 3
 print('ACME', 50, 91.5, sep=',', end='!!\n')

# Python 2
from __future__ import print_function
print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

#Python 3
print('.'.join('ACME','50','91.5'))

#Python 2
print('.'.join(['ACME','50','91.5']))

row = ('ACME', 50, 91.5)
print(','.join(row))

print('.'.join(str(x) for x in row))

print(*row, sep='.')



