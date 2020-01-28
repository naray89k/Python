#!/usr/bin/env python
# coding: utf-8

# ### Named Tuples - DocStrings and Default Values
from collections import namedtuple


# #### Adding DocStrings to Named Tuples

# This is easy to do, both with the generated class, as well as it's properties.
Point2D = namedtuple('Point2D', 'x y')

Point2D.__doc__ = 'Represents a 2D Cartesian coordinate'


# And we can even add docstrings to the properties:
Point2D.x.__doc__ = 'x-coordinate'
Point2D.y.__doc__ = 'y-coordinate'
help(Point2D)


# #### Adding Default Values to Named Tuples

# #### Using a Prototype

# This technique is in the Python docs, and uses the concept of creating a prototype object that has the default values set:
Vector = namedtuple('Vector', 'x1 y1 x2 y2 origin_x origin_y')
vector_zeroorigin = Vector(x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)
vector_zeroorigin


# The named tuple `vector_zeroorigin` is now a prototype of a vector with zero origin.
# To create new vectors using that origin as a default, we no longer use the `Vector` class, but instead use `_replace` as follows:
v1 = vector_zeroorigin._replace(x1=1, y1=1, x2=10, y2=10)
v1


# This certainly works, and can be useful in cases where you may want more than one prototype (e.g. `vector_zeroorigin` and `vector_otherorigin`)

# #### Using `__defaults__`

# There is an alternative way of doing this. And, in my opinion, a much cleaner alternative.

# In Python the default values for a function's parameters are stored as a tuple in the `__defaults__` attribute.
def func(a, b=20, c=30):
    print(a, b, c)

func.__defaults__
func(10)


# But the `__defaults__` property is writable:
func.__defaults__ = (200, 300)
func(10)


# In this case, the function we are interested in specifying default values for, is the named tuple class constructor, i.e. `__new__`.
# So, we will simply need to set `Vector.__new__.__defaults__` to the desired tuple of default values.
# The only thing to note is that if you specify less default values (say `m` values) than the total number of arguments (say `n` values, where `m < n`), then the defaults will apply to the **last** `m` values. Think of it as writing out your field names and default values on two lines, and right-aligning them. (If you specify more, then the values at the beginning are effectively ignored)
Vector.__new__.__defaults__ = (0, 0)


# Here I am basically setting default values for the last two elements only, i.e. `origin_x` and `origin_y`.
v1 = Vector(0, 0, 10, 10, -10, -10)
v1
v2 = Vector(5, 5, 20, 20)
v2
v3 = Vector(x1=1, y1=1, x2=10, y2=10)
v3


# An even simpler way to set default values if you want **all** the defaults to be the same:
Vector.__new__.__defaults__ = (0,) * len(Vector._fields)
v5 = Vector()
v5


# Of course, the usual admonishment of not using mutable default values holds here as well.
