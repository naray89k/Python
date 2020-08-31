#!/usr/bin/env python
# coding: utf-8
line = 'asdf fjdk; afed, fjek,asdf,       foo'
import re

re.split(r'[;,\s]\s*', line)

fields = re.split(r'(;|,|\s)\s*', line)
fields

values = fields[::2]
delimiters = fields[1::2] + ['']
values

delimiters

''.join(v + d for v, d in zip(values, delimiters))

re.split(r'(?:,|;|\s)\s*', line)
