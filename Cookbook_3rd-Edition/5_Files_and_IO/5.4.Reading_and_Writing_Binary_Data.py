#!/usr/bin/env python
# coding: utf-8
# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
     f.write(b'Hello World')

# Text string
t = 'Hello World'
t[0]

for i in t:
    print i

# Python 3
b = b'Hello World'
b[0]

#Python 3
for c in b:
    print(c)

#Python 2
ord(b[0])

#Python 2
for i in b:
    print ord(i)

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    
with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin','wb') as f:
    f.write(nums)

import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

a



