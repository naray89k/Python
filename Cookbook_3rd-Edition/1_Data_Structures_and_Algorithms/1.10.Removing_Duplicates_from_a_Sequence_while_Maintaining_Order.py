#!/usr/bin/env python
# coding: utf-8
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1,5,2,1,9,1,5,10]

print(list(dedupe(a))

a = [1,5,2,1,9,1,5,10]
b = []
for i in a:
    if i in b:
        pass
    else:
        b.append(i)
print(b)

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
b = []
for i in a:
    if i in b:
        pass
    else:
        b.append(i)
print(b)

a = [1,5,2,1,9,1,5,10]
set(a)



