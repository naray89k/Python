#!/usr/bin/env python
# coding: utf-8

# ### Callables

# A callable is an object that can be called (using the **()** operator), and always returns a value.
# We can check if an object is callable by using the built-in function **callable**

# ##### Functions and Methods are callable
callable(print)
callable(len)
l = [1, 2, 3]
callable(l.append)
s = 'abc'
callable(s.upper)


# ##### Callables **always** return a value:
result = print('hello')
print(result)
l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)

s = 'abc'
result = s.upper()
print(result)


# ##### Classes are callable:
from decimal import Decimal

callable(Decimal)
result = Decimal('10.5')
print(result)


# ##### Class instances may be callable:
class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0

    def __call__(self, x=1):
        self.counter += x
        print(self.counter)

my_obj = MyClass()
callable(my_obj.__init__)
callable(my_obj.__call__)
my_obj()
my_obj()
my_obj(10)
