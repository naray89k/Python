#!/usr/bin/env python
# coding: utf-8

# ### What's New in Python 3.6

# Here are just a few highlights.
# For the full monty (python), read it here:
# `https://docs.python.org/3/whatsnew/3.6.html`

# I will create some additional videos looking at each of these in more detail.

# #### Dictionaries maintain sort order

# Dictionaries will maintain their key order based on when items were inserted.
# This is an implementation detail in 3.6 (i.e. the behavior happens because of the new implementation of dicts, but not guaranteed in the sense that a future release could change that). However, there seems to be official confirmation from GvR that starting in 3.7 it will be guaranteed.
# If you use `prettyprint` be careful as that sorts the dictionary keys lexicographically before printing and this will still be the case in 3.7 (after much debate over it in the Python dev community!)

# #### Preserving Order of **kwargs in Function Arguments

# This is actually unrelated to the dict key order preservation.
# The order in which `**kwarg` arguments are passed to a function is retained when you iterate the `kwarg` parameter inside the called function.
# This is actually a big deal. I'll show you how this allows us to easily create a named tuple factory function with default values for example.

# #### Underscores in Numeric Literals

# This one is also really nice to help readability. You can now use underscores in numeric literals.
# For example:
1_000_000
0x_FFFF_FFFF


# #### f-Strings

# A much simpler string interpolation. You can embed Python expressions directly into strings (including multi-line) as well as the usual string formatting directives just by preceding the string with an `f` or `F`.
# For example:
numerator = 10
denominator = 3
response = f'{numerator}/{denominator} = {numerator / denominator:0.3f}'
print(response)


# #### Type Annotations

# Basically allows us to provide type information to function arguments, class variables, etc.
# More info in PEP 484 and PEP 526.

# According to PEP 484:
# "It should also be emphasized that **Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention**."

# Tools that make use of these type annotations include `mypy`, `PyCharm`. Probably others too.

# Here's an example of type annotations:
from typing import List

def squares(l: List[int]) -> List[int]:
    return [e ** 2 for e in l]

my_list: List[int] = [1, 2, 3, 4]
my_list, squares(my_list)


# But Python does not use those annotations - here I am passing a dictionary to the function (with integer keys so the function still works properly). Obviously dictionaries are not lists!
d = {1: 'a', 2: 'b', 3:'c', 4:'d'}
squares(d)


# The type annotations **do not affect** Python itself - it is simply a set of syntactic additions that allows **external** tools such as `mypy` or `PyCharm` to perform static type checking.

# #### Asynchronous Enhancements

# This is beyond the scope of Part 1, but really useful additions worth at least mentioning have been added to the Python language to better support asynchronous programming (I'll cover that in detail in subsequent parts of the course series - most likely Part 4)

# #### Plus a LOT more

# There's a lot more to really love in 3.6, and you can read all about it here:
# `https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep526`
