#!/usr/bin/env python
# coding: utf-8

# ## Everything is an Object
a = 10

# **a** is an object of type **int**, i.e. **a** is an instance of the **int** class.
print(type(a))

# If **int** is a class, we should be able to declare it using standard class instatiation:
b = int(10)
print(b)
print(type(b))


# We can even request the class documentation:
help(int)

# As we see from the docs, we can even create an **int** using an overloaded constructor:
b = int('10', base=2)
print(b)
print(type(b))

# ### Functions are Objects too
# ---
def square(a):
    return a ** 2

type(square)
f = square
type(f)

f is square
f(2)
type(f(2))


# A function can return a function
def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))
print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))


f = select_function(2)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))
print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))


# We could even call it this way:
select_function(1)(5)


# A Function can be passed as an argument to another function
# (This example is pretty useless, but it illustrates the point effectively)
def exec_function(fn, n):
    return fn(n)

result = exec_function(cube, 2)
print(result)

# We will come back to functions as arguments **many** more times throughout this course!
