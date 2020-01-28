#!/usr/bin/env python
# coding: utf-8
import sys
sys.getfilesystemencoding()

with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
import os
os.listdir('.')

# Directory listing (raw)
os.listdir(b'.') # Note: byte string

# Open file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

