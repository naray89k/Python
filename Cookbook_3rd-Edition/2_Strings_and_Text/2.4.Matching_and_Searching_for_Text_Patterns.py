#!/usr/bin/env python
# coding: utf-8
text = 'yeah, but no, but yeah, but no, but yeah'

text == 'yeah'

text.startswith('yeah')

text.endswith('no')

text.find('no')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2012')
m

m.group(0)

m.group(1)

m.group(2)

m.group(3)

m.groups()

text

datepat.findall(text)

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for m in datepat.finditer(text):
    print(m.groups())

m = datepat.match('11/27/2012abcdef')
m

m.group()

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')
datepat.match('11/27/2012')

re.findall(r'(\d+)/(\d+)/(\d+)', text)
