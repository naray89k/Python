#!/usr/bin/env python
# coding: utf-8
# Python 2
s1 = u'Spicy Jalape\u00f1o'
s2 = u'Spicy Jalapen\u0303o'
print(s1)

print(s2)

s1 == s2

len(s1)

len(s2)

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFD', s2)

t1 == t2

# python 3
print(ascii(t1))

# Python 2
print(t1)

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

t3 == t4

# Python 3
print(ascii(t3))

# Python 2
print(t3)

# Python 3
s = u'\ufb01'
print(s)

# Python 2
s = u'\ufb01'
t = unicodedata.normalize('NFD', s)

print(t)

print(unicodedata.normalize('NFKD', s))

print(unicodedata.normalize('NFKC', s))

t1 = unicodedata.normalize('NFD', s1)

''.join(c for c in t1 if not unicodedata.combining(c))
