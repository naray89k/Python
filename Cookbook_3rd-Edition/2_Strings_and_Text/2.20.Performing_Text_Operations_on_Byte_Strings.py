#!/usr/bin/env python
# coding: utf-8
data = b'Hello World'
data[0:5]

data.startswith(b'Hello')

data.split()

data.replace(b'Hello', b'Hello Cruel')

data = bytearray(b'Hello World')

data[0:5]

data.startswith(b'Hello')

data.split()

data.replace(b'Hello', b'Hello Cruel')

data = b'FOO:BAR,SPAM'

import re
re.split('[:,]',data)

a = 'Hello World' # Text string
print(a[0])
print(a[1])

b = b'Hello World' 

print(b[0])
print(b[1])

s = b'Hello World'
print(s)
print(s.decode('ascii'))

