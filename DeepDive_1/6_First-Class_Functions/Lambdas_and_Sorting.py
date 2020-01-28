#!/usr/bin/env python
# coding: utf-8

# ### Lambdas and Sorting

# Python has a built-in **sorted** method that can be used to sort any iterable. It will use the default ordering of the particular items, but sometimes you may want to (or need to) specify a different criteria for sorting.

# Let's start with a simple list:
l = ['a', 'B', 'c', 'D']
sorted(l)


# As you can see there is a difference between upper and lower-case characters when sorting strings.
# What if we wanted to make a case-insensitive sort?
# Python's **sorted** function kas a keyword-only argument that allows us to modify the values that are used to sort the list.
sorted(l, key=str.upper)


# We could have used a lambda here (but you should not, this is just to illustrate using a lambda in this case):
sorted(l, key = lambda s: s.upper())


# Let's look at how we might create a sorted list from a dictionary:
d = {'def': 300, 'abc': 200, 'ghi': 100}
d
sorted(d)


# What happened here?
# Remember that iterating dictionaries actually iterates the keys - so we ended up with tyhe keys sorted alphabetically.
# What if we want to return the keys sorted by their associated value instead?
sorted(d, key=lambda k: d[k])


# Maybe we want to sort complex numbers based on their distance from the origin:
def dist(x):
    return (x.real)**2 + (x.imag)**2

l = [3+3j, 1+1j, 0]


# Trying to sort this list directly won't work since Python does not have an ordering defined for complex numbers:
sorted(l)


# Instead, let's try to specify the key using the distance:
sorted(l, key=dist)


# Of course, if we're only going to use the **dist** function once, we can just do the same thing this way:
sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2)


# And here's another example where we want to sort a list of strings based on the **last character** of the string:
l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
sorted(l)
sorted(l, key=lambda s: s[-1])
