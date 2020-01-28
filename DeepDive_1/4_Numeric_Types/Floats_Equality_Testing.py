#!/usr/bin/env python
# coding: utf-8

# ## Floats - Equality Testing

# Because not all real numbers have an exact ``float`` representation, equality testing can be tricky.
x = 0.1 + 0.1 + 0.1
y = 0.3
x == y


# This is because ``0.1`` and ``0.3`` do not have exact representations:
print('0.1 --> {0:.25f}'.format(0.1))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))


# However, in some (limited) cases where all the numbers involved do have an exact representation, it will work:
x = 0.125 + 0.125 + 0.125
y = 0.375
x == y

print('0.125 --> {0:.25f}'.format(0.125))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))


# One simple way to get around this is to round to a specific number of digits and then compare
x = 0.1 + 0.1 + 0.1
y = 0.3
round(x, 5) == round(y, 5)


# We can also use a more flexible technique implemented by the ``isclose`` method in the ``math`` module
from math import isclose

help(isclose)

x = 0.1 + 0.1 + 0.1
y = 0.3
isclose(x, y)


# The ``isclose`` method takes two optional parameters, ``rel_tol`` and ``abs_tol``.
# ``rel_tol`` is a relative tolerance that will be relative to the magnitude of the largest of the two numbers being compared. Useful when we want to see if two numbers are close to each other as a percentage of their magnitudes.
# ``abs_tol`` is an absolute tolerance that is independent of the magnitude of the numbers we are comparing - this is useful for numbers that are close to zero.

# In this situation we might consider x and y to be close to each other:
x = 123456789.01
y = 123456789.02


# but not in this case:
x = 0.01
y = 0.02


# In both these cases the difference between the two numbers was ``0.01``, yet in one case we considered the numbers "equal" and in the other, not "equal". Relative tolerances are useful to handle these scenarios.
isclose(123456789.01, 123456789.02, rel_tol=0.01)

isclose(0.01, 0.02, rel_tol=0.01)


# On the other hand, we have to be careful with relative tolerances when working with values that are close to zero:
x = 0.0000001
y = 0.0000002
isclose(x, y, rel_tol=0.01)


# So, we could use an absolute tolerance here:
isclose(x, y, abs_tol=0.0001, rel_tol=0)


# In general, we can combine the use of both relative and absolute tolerances in this way:
x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))

