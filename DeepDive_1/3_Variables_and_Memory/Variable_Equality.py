#!/usr/bin/env python
# coding: utf-8

# ## Variable Equality
# From the previous lecture we know that **a** and **b** will have a **shared** reference:
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))


# When we use the **is** operator, we are comparing the memory address **references**:
print("a is b: ", a is b)

# But if we use the **==** operator, we are comparing the **contents**:
print("a == b:", a == b)

# The following however, do not have a shared reference:
a = [1, 2, 3]
b = [1, 2, 3]
print(hex(id(a)))
print(hex(id(b)))

# Although they are not the same objects, they do contain the same "values":
print("a is b: ", a is b)
print("a == b", a == b)

# Python will attempt to compare values as best as possible, for example:
a = 10
b = 10.0

# These are **not** the same reference, since one object is an **int** and the other is a **float**
print(type(a))
print(type(b))

print(hex(id(a)))
print(hex(id(b)))

print('a is b:', a is b)
print('a == b:', a == b)

# So, even though *a* is an integer 10, and *b* is a float 10.0, the values will still compare as equal.
# In fact, this will also have the same behavior:
c = 10 + 0j
print(type(c))

print('a is c:', a is c)
print('a == c:', a == c)


# ### The None Object
# ----
# **None** is a built-in "variable" of type *NoneType*.
# Basically the keyword **None** is a reference to an object instance of *NoneType*.
# NoneType objects are immutable! Python's memory manager will therefore use shared references to the None object.
print(None)
hex(id(None))
type(None)
a = None
print(type(a))
print(hex(id(a)))
a is None
a == None
b = None
hex(id(b))
a is b
a == b
l = []
type(l)
l is None
l == None

