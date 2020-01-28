#!/usr/bin/env python
# coding: utf-8

# ### Lambda Expressions
lambda x: x**2


# As you can see, the above expression just created a function.

# #### Assigning to a Variable
func = lambda x: x**2
type(func)
func(3)


# We can specify arguments for lambdas just like we would for any function created using **def**, except for annotations:
func_1 = lambda x, y=10: (x, y)
func_1(1, 2)
func_1(1)


# We can even use \* and \*\*:
func_2 = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})
func_2(1, 'a', 'b', y=100, a=10, b=20)


# #### Passing as an Argument

# Lambdas are functions, and can therefore be passed to any other function as an argument (or returned from another function)
def apply_func(x, fn):
    return fn(x)

apply_func(3, lambda x: x**2)
apply_func(3, lambda x: x**3)


# Of course we can make this even more generic:
def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

apply_func(lambda x, y: x+y, 1, 2)
apply_func(lambda x, *, y: x+y, 1, y=2)
apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)


# Of course in the example above, we really did not need to create a lambda!
apply_func(sum, (1, 2, 3, 4, 5))


# Of course, we don't have to use lambdas when calling **apply_func**, we can also pass in a function defined using a **def** statement:
def multiply(x, y):
    return x * y

apply_func(multiply, 'a', 5)
apply_func(lambda x, y: x*y, 'a', 5)
