#!/usr/bin/env python
# coding: utf-8
import os
os.path.exists('/etc/passwd')

os.path.exists('/tmp/spam')

os.path.isfile('/etc/passwd')

os.path.isdir('/etc/passwd')

os.path.islink('/usr/local/bin/python3')

os.path.realpath('/usr/local/bin/python3')

os.path.getsize('/etc/passwd')

os.path.getmtime('/etc/passwd')

import time
time.ctime(os.path.getmtime('/etc/passwd'))

os.path.getsize('/Users/guido/Desktop/foo.txt')

