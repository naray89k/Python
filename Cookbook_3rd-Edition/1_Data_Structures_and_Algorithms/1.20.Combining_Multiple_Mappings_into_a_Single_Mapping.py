#!/usr/bin/env python
# coding: utf-8
#Python 3
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

import sys
get_ipython().system('{sys.executable} -m pip install chainmap')

#Python 2 NB::you might need to install chainmap module
from chainmap import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

len(c)

list(c.keys())

list(c.values())

c['z'] = 10
c['w'] = 40
del c['x']

c

del c['y']

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
values

values['x']

values = values.parents

values['x']

values = values.parents

values['x']

values

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = dict(b)
merged.update(a)
merged

merged['x']

merged['y']

merged['z']

a['x'] = 13
merged['x']

a = {'x':1,'z':3}
b = {'y':2,'z':4}
merged = ChainMap(a,b)
merged['x']

a['x'] = 42
merged['x']



