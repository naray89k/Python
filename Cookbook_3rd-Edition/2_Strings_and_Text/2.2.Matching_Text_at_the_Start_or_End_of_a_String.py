#!/usr/bin/env python
# coding: utf-8
filename = 'spam.txt'
filename.endswith('.txt')

filename.startswith('file:')

url = 'http://www.python.org'
url.startswith('http:')

import os
filename = os.listdir('.')
filename

[name for name in filename if name.endswith('ipynb')]
any(name.endswith('ipynb') for name in filename)

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:','ftp:']
url = 'http://www.python.org'
url.startswith(choices)

url.startswith(tuple(choices))

filename = 'spam.txt'
filename[-4:] == '.txt'

url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4]=='ftp:'

import re
url = 'http://www.python.org'
print bool(re.match('http:|https:|ftp:', url))



