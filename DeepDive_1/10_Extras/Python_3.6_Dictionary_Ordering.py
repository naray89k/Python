#!/usr/bin/env python
# coding: utf-8

# ### Python 3.6 - Dictionary Ordering

# Python 3.6 sees a new implementation of the standard `dict` that preserves key ordering (based on the order in which new keys are added into or removed from the dictionary)

# Although this is an implementation detail in 3.6, it is supposed to become official in Python 3.7.
# `https://mail.python.org/pipermail/python-dev/2017-December/151283.html`
# So it should be safe to now assume dictionary keys will retain order , and using an `OrderedDict` might no longer be needed for certain cases. I'll come back to `OrderedDict` in a bit...
# **Use for Python 3.6 and higher only!**
# If you use that ordering feature with standard `dict` objects and then try to run your code in a prior version, things will break :-)

# Also means that `keys()` (that iterate from left to right) preserves order as does `values()`. On the other hand `popitem()` will pop right-most element from dictionary. Sounds like stack behavior to me - but does not mean you should use it as such - I'm pretty sure that's not going to be as efficient as say using a list!.

# Let's see some of this (just make sure you're running 3.6 or higher)
from sys import version_info

version_info

d = {'a': 1, 'b': 2}

d.keys(), d.values(), d.items()

d['x'] = 3

d.keys(), d.values(), d.items()

del d['b']

d.keys(), d.values(), d.items()

d['b'] = 4

d.keys(), d.values(), d.items()


# What about replacing a value for an existing key?
d['x'] =100

d.keys(), d.values(), d.items()


# Order maintained...

# And if we pop:
d.popitem()


# We popped the last item.

# So now I'm left wondering how to pick a *random* item from the dictionary?
# (Not that we could before - it might have looked random when we popped an item but it wasn't)
# Sounds like another video :-)

# **Important note:** Be careful of Jupyter notebooks - something I just realized - take a look:
d = {'x': 1, 'a': 2}
print(d)
d


# Notice how just letting Jupyter display `d` changed the display order of the keys? (I'm guessing its doing something similar to `prettyprint` (or maybe even using it), which changes the displayed key order to be lexicographical.

# What about using `update` to update one dict based on another (inserting missing keys, and updating common ones - but especially the insertion bit) - I'm guessing the order is retained with any insertions appearing at the end and ordered according to the dict being merged in. Let's see:
d1 = {'a': 1, 'b': 200}
d2 = {'a': 100, 'd':300, 'c':400}
d1.update(d2)
print(d1)


# Back to `OrderedDict` for a second:

# `OrderedDict` has a few methods that afaik have no equivalent (yet) in standard dicts:
# * `move_to_end(key, last=True)` - either move to front or back
# * `popitem(last=True)` - that can pop either from front or back of dict
# * supports reverse iteration using `reversed()`

# Let's take each one of those one by one:

# **move to end:**
d = {'a':1, 'b':2, 'c':3}
print('start:', d)
d['a'] = d.pop('a')
print('moved a to end:',d)


# **move to front:**

# That's one not so easy, the only option I can think of is to move all the keys around to re-order. Maybe something like this:
d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start:', d)
d['c'] = d.pop('c')
print('moved c to end:', d)

for i in range(len(d)-1):
    key = next(iter(d.keys()))
    d[key] = d.pop(key)
print('moved c to front:', d)


# **pop last item:**

# That one's trivial - just use `popitem`:
d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start:', d)
d.popitem()
print('pop last item:', d)


# **pop first item:**

# Not too difficult - we just need to identify the *first* key, and pop it.
d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start:', d)
key = next(iter(d.keys()))
d.pop(key)
print('pop first item:', d)


# If you're interested, here's Raymond Hettinger's pure Python "version" of his C dict implementation:
# `http://code.activestate.com/recipes/578375/`
