#!/usr/bin/env python
# coding: utf-8

# ## Variable Re-Assignment

# Notice how the memory address of **a** is different every time.

a = 10
hex(id(a))

a = 15
hex(id(a))

a = 5
hex(id(a))

a = a + 1
hex(id(a))


# However, look at this:
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))


# The memory addresses of both **a** and **b** are the same!! 
