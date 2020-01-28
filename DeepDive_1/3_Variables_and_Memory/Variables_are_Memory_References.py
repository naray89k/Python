#!/usr/bin/env python
# coding: utf-8

# ## Variables are Memory References

# We can find the memory address that a variable *references*, by using the `id()` function.
# The `id()` function returns the memory address of its argument as a base-10 integer.
# We can use the function `hex()` to convert the base-10 number to base-16.

my_var = 10
print('my_var = {0}'.format(my_var))
print('memory address of my_var (decimal): {0}'.format(id(my_var)))
print('memory address of my_var (hex): {0}'.format(hex(id(my_var))))


greeting = 'Hello'
print('greeting = {0}'.format(greeting))
print('memory address of my_var (decimal): {0}'.format(id(greeting)))
print('memory address of my_var (hex): {0}'.format(hex(id(greeting))))


# Note how the memory address of `my_var` is **different** from that of `greeting`.
# Strictly speaking, `my_var` is not "equal" to 10. 
# Instead `my_var` is a **reference** to an (*integer*) object (*containing the value 10*) located at the memory address `id(my_var)`
# Similarly for the variable `greeting`.
