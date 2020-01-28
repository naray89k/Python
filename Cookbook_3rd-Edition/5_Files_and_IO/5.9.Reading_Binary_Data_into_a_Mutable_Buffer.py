#!/usr/bin/env python
# coding: utf-8
import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# Write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
buf

buf[0:5] = b'Hallo'
buf

with open('newsample.bin', 'wb') as f:
    f.write(buf)

record_size = 32 # Size of each record (adjust value)
buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
 # Use the contents of buf

buf

m1 = memoryview(buf)
m2 = m1[-5:]
m2

m2[:] = b'WORLD'
buf

