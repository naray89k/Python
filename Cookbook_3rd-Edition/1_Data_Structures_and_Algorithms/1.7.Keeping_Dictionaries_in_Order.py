#!/usr/bin/env python
# coding: utf-8
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

print(d)

e = {} #regular dictionary does not order input
e['foo'] = 1
e['bar'] = 2
e['spam'] = 3
e['grok'] = 4

print(e)

for key, value in d.items():
    print key, value

import json
json.dumps(d)



