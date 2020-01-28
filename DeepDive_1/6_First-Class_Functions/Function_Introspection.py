#!/usr/bin/env python
# coding: utf-8

# ### Function Introspection
def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n

    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n-1)


# Since functions are objects, we can add attributes to a function:
fact.short_description = "factorial function"

print(fact.short_description)


# We can see all the attributes that belong to a function using the **dir** function:
dir(fact)


# We can see our **short_description** attribute, as well as some attributes we have seen before: **__annotations__** and **__doc__**:
fact.__doc__

fact.__annotations__


# We'll revisit some of these attributes later in this course, but let's take a look at a few here:
def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass


# Let's assign my_func to another variable:
f = my_func


# The **__name__** attribute holds the function's name:
my_func.__name__

f.__name__


# The **__defaults__** attribute is a tuple containing any positional parameter defaults:
my_func.__defaults__

my_func.__kwdefaults__


# Let's create a function with some local variables:
def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func('a', 100)

# The **__code__** attribute contains a **code** object:
my_func.__code__

# This **code** object itself has various properties:
dir(my_func.__code__)


# Attribute **__co_varnames__** is a tuple containing the parameter names and local variables:
my_func.__code__.co_varnames


# Attribute **co_argcount** returns the number of arguments (minus any \* and \*\* args)
my_func.__code__.co_argcount


# #### The **inspect** module

# It is much easier to use the **inspect** module!
import inspect

inspect.isfunction(my_func)


# By the way, there is a difference between a function and a method! A method is a function that is bound to some object:
inspect.ismethod(my_func)

class MyClass:
    def f_instance(self):
        pass

    @classmethod
    def f_class(cls):
        pass

    @staticmethod
    def f_static():
        pass


# **Instance methods** are bound to the **instance** of a class (not the class itself)

# **Class methods** are bound to the **class**, not instances

# **Static methods** are no bound either to the class or its instances
inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance)
inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class)
inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static)
my_obj = MyClass()
inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance)
inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class)
inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static)


# If you just want to know if something is a function or method:
inspect.isroutine(my_func)
inspect.isroutine(MyClass.f_instance)
inspect.isroutine(my_obj.f_class)
inspect.isroutine(my_obj.f_static)


# We'll revisit this in more detail in section on OOP.

# #### Introspecting Callable Code

# We can get back the source code of our function using the **getsource()** method:
inspect.getsource(fact)
print(inspect.getsource(fact))
inspect.getsource(MyClass.f_instance)
inspect.getsource(my_obj.f_instance)


# We can also find out where the function was defined:
inspect.getmodule(fact)
inspect.getmodule(print)

import math
inspect.getmodule(math.sin)

# setting up variable
i = 10

# comment line 1
# comment line 2
def my_func(a, b=1):
    # comment inside my_func
    pass

inspect.getcomments(my_func)
print(inspect.getcomments(my_func))


# #### Introspecting Callable Signatures
# TODO: Provide implementation
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg' = 10,
            **kwargs: 'additional keyword-only args') -> str:
    """does something
       or other"""
    pass

inspect.signature(my_func)
type(inspect.signature(my_func))
sig = inspect.signature(my_func)
dir(sig)

for param_name, param in sig.parameters.items():
    print(param_name, param)

def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')
    print('{0}\n{1}\n'.format(inspect.getcomments(f),
                              inspect.cleandoc(f.__doc__)))
    print('{0}\n{1}'.format('Inputs', '-'*len('Inputs')))

    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')

    print('{0}\n{1}'.format('\n\nOutput', '-'*len('Output')))
    print(sig.return_annotation)

print_info(my_func)


# #### A Side Note on Positional Only Arguments

# Some built-in callables have arguments that are positional only (i.e. cannot be specified using a keyword).
# However, Python does not currently have any syntax that allows us to define callables with positional only arguments.
# In general, the documentation uses a **/** character to indicate that all preceding arguments are positional-only. But not always :-(
help(divmod)


# Here we see that the **divmod** function takes two positional-only parameters:
divmod(10, 3)
divmod(x=10, y=3)


# Similarly, the string **replace** function also takes positional-only arguments, however, the documentation does not indicate this!
help(str.replace)

'abcdefg'.replace('abc', 'xyz')
'abcdefg'.replace(old='abc', new='xyz')
