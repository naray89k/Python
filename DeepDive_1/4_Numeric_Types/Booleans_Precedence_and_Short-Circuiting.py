#!/usr/bin/env python
# coding: utf-8

# ### Booleans: Precedence and Short-Circuiting
True or True and False

# this is equivalent, because of ``and`` having higer precedence than ``or``, to:
True or (True and False)

# This is not the same as:
(True or True) and False

# #### Short-Circuiting
a = 10
b = 2

if a/b > 2:
    print('a is at least double b')

a = 10
b = 0

if a/b > 2:
    print('a is at least double b')

a = 10
b = 0

if b and a/b > 2:
    print('a is at least double b')

# Can also be useful to deal with null or empty strings in a database:
import string

help(string)

string.digits

string.ascii_letters

name = ''
if name[0] in string.digits:
    print('Name cannot start with a digit!')

name = ''
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

name = None
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

name = 'Bob'
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

name = '1Bob'
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')
