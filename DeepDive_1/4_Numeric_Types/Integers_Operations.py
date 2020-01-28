#!/usr/bin/env python
# coding: utf-8

# ## Integers - Operations

# Addition, subtraction, multiplication and exponentiation of integers always result in an integer.
type(2 + 3)
type(3 - 10)
type(3 * 5)
type(3 ** 4)


# But the standard division operator `/` **always** results in a float value.
type(2 / 3)
type(10 / 2)


# The `math.floor()` method will return the floor of any number.
import math


# For non-negative values (>= 0), the floor of the value is the same as the integer portion of the value (truncation)
math.floor(3.15)
math.floor(3.9999999)


# However, this is not the case for negative values:
math.floor(-3.15)
math.floor(-3.0000001)


# #### The Floor Division Operator

# The floor division operator `a//b` is the floor of `a / b`
# i.e. `a // b = math.floor(a / b)`
# This is true whether `a` and `b` are positive or negative.
a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))


# For positive numbers, `a//b` is basically the same as truncating (taking the integer portion) of `a / b`.

# But this is **not** the case for negative numbers.
a = -33
b = 16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))

a = 33
b = -16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))


# #### The Modulo Operator

# The modulo operator and the floor division operator will always satisfy the following equation:
# ``a = b * (a // b) + a % b``
a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

