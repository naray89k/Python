#!/usr/bin/env python
# coding: utf-8
#Python 3 code

a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}

b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}

a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

c = {key:a[key] for key in a.keys() - {'z','w'}}

print(c)

# Python 2 code
a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}

b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}

c = set()

for i in a.keys():
    for j in b.keys():
        if i in j:
            c.add(i)
print(c)
print(set(a.keys())-c)
print (list(set(a.keys()) - c)+list(set(b.keys())-c))

d = {}
for i, j in a.items():
    for k, m in b.items():
        if i == k:
            a

# Python 2 code
e = {}
for i,j in a.items():
    if i != 'z' and i != 'w':
        e[i] = j
print(e)



