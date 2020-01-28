#!/usr/bin/env python
# coding: utf-8
s = '{name} has {n} messages.'
s.format(name='Guido', n = 37)

name = 'Guido'
n = 37
s.format_map(vars())

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido',37)
s.format_map(vars(a))

s.format(name='Guido')

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
s.format_map(safesub(vars()))

import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print sub('Hello {name}')

print sub('You have {n} messages.')

print sub('Your favorite color is {color}')

name = 'Guido'
n = 37
'%(name) has %(n) messages.'%vars()

import string
s = string.Template('$name has $n messages.')
s.substitute(vars())



