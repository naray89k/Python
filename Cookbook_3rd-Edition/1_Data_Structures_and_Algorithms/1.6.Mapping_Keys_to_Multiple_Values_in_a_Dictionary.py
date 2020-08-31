#!/usr/bin/env python
# coding: utf-8
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

for key, value in d.items():
    for i in value:
        print(key, i)

for key, value in e.items():
    for i in value:
        print(key, i)

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(3)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(5)

print(d)

d = {}

for key, value in pairs.items():
    print(key, value)
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)

d = {}
for key, value in pairs.items():
    d.setdefault(key, []).append(value)
print(d)
