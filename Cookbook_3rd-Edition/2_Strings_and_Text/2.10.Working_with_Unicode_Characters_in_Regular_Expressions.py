#!/usr/bin/env python
# coding: utf-8
import re

num = re.compile('\d+')
num.match('123')

print(num.match('u\u0661\u0662\u0663'))

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

print(arabic)

pat = re.compile(u'stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)

pat.match(s.upper())

s.upper()





