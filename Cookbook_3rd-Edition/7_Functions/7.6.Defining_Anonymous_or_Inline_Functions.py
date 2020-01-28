#!/usr/bin/env python
# coding: utf-8
add = lambda x, y: x + y

add(2,3)

add('hello', 'world')

def add(x,y):
    return x + y

add(2,3)

names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())



