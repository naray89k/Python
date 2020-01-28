#!/usr/bin/env python
# coding: utf-8

# ### Booleans: Boolean Operators

# The way the Boolean operators ``and``, ``or`` actually work is a littel different in Python:
# #### or
# ``X or Y``: If X is falsy, returns Y, otherwise evaluates and returns X
'' or 'abc'
0 or 100
[] or [1, 2, 3]
[1, 2] or [1, 2, 3]


# You should note that the truth value of ``Y`` is never even considered when evaluating the ``or`` result!
# Only the left operand matters.
# Of course, Y will be evaluated if it is being returned - but its truth value does not affect how the ``or`` is being calculated.
# You probably will notice that this means ``Y`` is not evaluated if ``X`` is returned - short-circuiting!!!
# We could (almost!) write the ``or`` operator ourselves in this way:
def _or(x, y):
    if x:
        return x
    else:
        return y

print(_or(0, 100) == (0 or 100))
print(_or(None, 'n/a') == (None or 'n/a'))
print(_or('abc', 'n/a') == ('abc' or 'n/a'))


# Why did I say almost?
# Unlike the ``or`` operator, our ``_or`` function will always evaluate x and y (they are passed as arguments) - so we do not have short-circuiting!
1 or 1/0
_or(1, 1/0)


# #### and
# `X and Y`: If X is falsy, returns X, otherwise evaluates and returns Y
# Once again, note that the truth value of Y is never considered when evaluating `and`, and that ``Y`` is only evaluated if it needs to be returned (short-circuiting)
s1 = None
s2 = ''
s3 = 'abc'

print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])

print((s1 and s1[0]) or '')
print((s2 and s2[0]) or '')
print((s3 and s3[0]) or '')


# This technique will also work to return any default value if ``s`` is an empty string or None:
print((s1 and s1[0]) or 'n/a')
print((s2 and s2[0]) or 'n/a')
print((s3 and s3[0]) or 'n/a')


# The ``not`` function
not 'abc'
not []
bool(None)
not None

