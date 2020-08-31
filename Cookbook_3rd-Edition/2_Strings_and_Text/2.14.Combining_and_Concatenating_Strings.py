#!/usr/bin/env python
# coding: utf-8
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)

','.join(parts)

''.join(parts)

a = 'Is Chicago'
b = 'Not Chicagoo?'
a + ' ' + b

print('{}{}'.format(a, b))

print(a + ' ' + b)

a = 'Hello' 'World'
a

s = ''
for p in parts:
    s += p
s

data = ['ACME', 50, 91.1]
','.join(str(d) for d in data)

print(a + ':' + b + ':' + c)
print(':'.join([a, b, c]))
print(a, b, c, sep=':')

from __future__ import print_function

print('Abac', 'Adndkg', sep=' ')

f.write(chunk1 + chunk2)
f.write(chunk1)
f.write(chunk2)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())

for part in sample():
    f.write(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    f.write(part)
