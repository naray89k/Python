#!/usr/bin/env python
# coding: utf-8

# ### Functions
# Python has many built-in functions and methods we can use
# Some are available by default:
s = [1, 2, 3]
len(s)

# While some need to be imported:
from math import sqrt
sqrt(4)

# Entire modules can be imported:
import math
math.exp(1)

# We can define our own functions:
def func_1():
    print('running func1')

func_1()

# Note that to "call" or "invoke" a function we need to use the **()**.
# Simply using the function name without the **()** refers to the function, but does not call it:
func_1

# We can also define functions that take parameters:
def func_2(a, b):
    return a * b

# Note that **a** and **b** can be any type (this is an example of polymorphism - which we will look into more detail later in this course). 
# But the function will fail to run if **a** and **b** are types that are not "compatible" with the ***** operator:
func_2(3, 2)
func_2('a', 3)
func_2([1, 2, 3], 2)
func_2('a', 'b')

# It is possible to use **type annotations**:
def func_3(a: int, b:int):
    return a * b

func_3(2, 3)
func_3('a', 2)

# But as you can see, these do not enforce a data type! They are simply metadata that can be used by external libraries, and many IDE's.
# Functions are objects, just like integers are objects, and they can be assigned to variables just as an integer can:
my_func = func_3
my_func('a', 2)

# Functions **must** always return something. If you do not specify a return value, Python will automatically return the **None** object:
def func_4():
    # does something but does not return a value
    a = 2

res = func_4()
print(res)


# The **def** keyword is an executable piece of code that creates the function (an instance of the **function** class) and 
# essentially assigns it to a variable name (the function **name**). 
# Note that the function is defined when **def** is reached, but the code inside it is not evaluated until the function is called.
# This is why we can define functions that call other functions defined later. 
# As long as we don't call them before all the necessary functions are defined.

# For example, the following will work:

def fn_1():
    fn_2()

def fn_2():
    print('Hello')

fn_1()

# But this will not work:
def fn_3():
    fn_4()

fn_3()

def fn_4():
    print('Hello')

# We also have the **lambda** keyword, that also creates a new function, but does not assign it to any specific name - instead it just returns the function object - which we can, if we wish, assign to a variable ourselves:
func_5 = lambda x: x**2
func_5(2)
