#!/usr/bin/env python
# coding: utf-8

# ## Multi-Line Statements and Strings
# Certain physical newlines are ignored in order to form a complete logical line of code.
# #### Implicit Examples
a = [1,
    2,
    3]
a


# You may also add comments to the end of each physical line:
a = [1, #first element
    2, #second element
    3, #third element
    ]
a


# Note if you do use comments, you must close off the collection on a new line.
# i.e. the following will not work since the closing ] is actually part of the comment:
a = [1, # first element
    2 #second element]

# This works the same way for tuples, sets, and dictionaries.
a = (1, # first element
    2, #second element
    3, #third element
    )
a

a = {1, # first element
    2, #second element
    }
a

a = {'key1': 'value1', #comment,
    'key2': #comment
    'value2' #comment
    }
a


# We can also break up function arguments and parameters:

def my_func(a, #some comment
           b, c):
    print(a, b, c)


my_func(10, #comment
       20, #comment
       30)

# #### Explicit Examples
# You can use the ``\`` character to explicitly create multi-line statements.

a = 10
b = 20
c = 30
if a > 5     and b > 10     and c > 20:
    print('yes!!')


# The identation in continued-lines does not matter:
a = 10
b = 20
c = 30
if a > 5     and b > 10         and c > 20:
    print('yes!!')


# #### Multi-Line Strings
# You can create multi-line strings by using triple delimiters (single or double quotes)
a = '''this is
a multi-line string'''
print(a)


# Note how the newline character we typed in the multi-line string was preserved. Any character you type is preserved. You can also mix in escaped characters line any normal string.
a = """some items:\n
    1. item 1
    2. item 2"""
print(a)


# Be careful if you indent your multi-line strings - the extra spaces are preserved!
def my_func():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a

print(my_func())

def my_func():
    a = '''a multi-line string
that is not indented in the second line'''
    return a

print(my_func())


# Note that these multi-line strings are **not** comments - they are real strings and, unlike comments, are part of your compiled code. They are however sometimes used to create comments, such as ``docstrings``, that we will cover later in this course.
# In general, use ``#`` to comment your code, and use multi-line strings only when actually needed (like for docstrings).
# Also, there are no multi-line comments in Python. You simply have to use a ``#`` on every line.

# this is
#    a multi-line
#    comment


# The following works, but the above formatting is preferrable.

# this is
    # a multi-line
    # comment

