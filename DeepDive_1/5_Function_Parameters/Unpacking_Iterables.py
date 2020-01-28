#!/usr/bin/env python
# coding: utf-8

# ### Unpacking Iterables

# #### Side Note on Tuples

# This is a tuple:
a = (1, 2, 3)

type(a)


# This is also a tuple:
a = 1, 2, 3

type(a)


# In fact what defines a tuple is not **()**, but the **,** (comma)

# To create a tuple with a single element:
a = (1)


# will not work!!
type(a)


# Instead, we have to use a comma:
a = (1,)

type(a)


# And in fact, we don't even need the **()**:
a = 1,

type(a)


# The only exception is to create an empty tuple:
a = ()

type(a)


# Or we can use the tuple constructor:
a = tuple()

type(a)


# #### Unpacking

# Unpacking is a way to split an iterable object into individual variables contained in a list or tuple: 
l = [1, 2, 3, 4]

a, b, c, d = l

print(a, b, c, d)


# Strings are iterables too:
a, b, c = 'XYZ'
print(a, b, c)


# #### Swapping Two Variables

# Here's a quick application of unpacking to swap the values of two variables.

# First we look at the "traditional" way you would have to do it in other languages such as Java:
a = 10
b = 20
print("a={0}, b={1}".format(a, b))

tmp = a
a = b
b = tmp
print("a={0}, b={1}".format(a, b))


# But using unpacking we can simplify this:
a = 10
b = 20
print("a={0}, b={1}".format(a, b))

a, b = b, a
print("a={0}, b={1}".format(a, b))


# In fact, we can even simplify the initial assignment of values to a and b as follows:
a, b = 10, 20
print("a={0}, b={1}".format(a, b))

a, b = b, a
print("a={0}, b={1}".format(a, b))


# #### Unpacking Unordered Objects
dict1 = {'p': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}

dict1

for c in dict1:
    print(c)

a, b, c, d, e, f = dict1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Note that this order is not guaranteed. You can always use an OrderedDict if that is a requirement.

# The same applies to sets.
s = {'p', 'y', 't', 'h', 'o', 'n'}

type(s)

print(s)

for c in s:
    print(c)

a, b, c, d, e, f = s

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

