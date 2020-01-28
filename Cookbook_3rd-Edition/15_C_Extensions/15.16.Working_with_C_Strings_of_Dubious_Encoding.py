#!/usr/bin/env python
# coding: utf-8
s = retstr()
s

print_chars(s)

raw = b'Spicy Jalape\xc3\xb1o\xae'
raw.decode('utf-8','ignore')

raw.decode('utf-8','replace')

raw.decode('utf-8','surrogateescape')

s = raw.decode('utf-8', 'surrogateescape')
print(s)

s

s.encode('utf-8','surrogateescape')

