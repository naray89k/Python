#!/usr/bin/env python
# coding: utf-8
from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')

fnmatch('foo.txt', '?oo.txt')

fnmatch('Dat45.csv', 'Dat[0-9]*')

names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
print [name for name in names if fnmatch(name,'Dat*.csv')]
print [name for name in names if not fnmatch(name,'*.py')]

#On Windows
fnmatch('foo.txt', '*.TXT')

#It is false on Mac OS

fnmatchcase('foo.txt','*.TXT')

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr,'* ST')]

[addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')]



