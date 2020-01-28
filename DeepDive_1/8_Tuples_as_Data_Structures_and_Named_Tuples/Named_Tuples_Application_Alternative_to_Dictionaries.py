#!/usr/bin/env python
# coding: utf-8

# ### Named Tuples - Application - Alternative to Dictionaries

# First an important caveat: all this really only works for dictionaries with **string** keys. Dictionary keys can be other hashable data types, (including tuples, as long as they contain hashable types in turn), and these examples will not work with those types of dictionaries.
from collections import namedtuple
data_dict = dict(key1=100, key2=200, key3=300)
Data = namedtuple('Data', data_dict.keys())
Data._fields


# Now we can create an instance of the `Data` named tuple using the data in the `data_dict` dictionary.
# We could try the following (bad idea):
d1 = Data(*data_dict.values())
d1


# This looks like it worked.
# But consider this second dictionary, where we do not create the keys in the same order:
data_dict_2 = dict(key1=100, key3=300, key2=200)
d2 = Data(*data_dict_2.values())
d2


# Obviously this went terribly wrong!
# We cannot guarantee that the order of `values()` will be in the same order as the keys (in our named tuple and in the dictionary).
# Instead, we should unpack the dictionary itself, resulting in keyword arguments that will be passed to the `Data` constructor:
d2 = Data(**data_dict_2)
d2


# So, the pattern to create a named tuple out of a single dictionary is straightforward:
# For any dictionary `d` we can created a named tuple class and insert the data into it as follows:
# `1. Struct = namedtuple('Struct', d.keys())`
# `2. data = Struct(**d)`

# Because dictionaries now preserve key order, the order of the fields in the named tuple structure will be the same. If you want your fields to be sorted in a different way, just sort the keys when you create the named tuple class. For example, to have keys sorted alphabetically we could do:
data_dict = dict(first_name='John', last_name='Cleese', age=42, complaint='dead parrot')
data_dict.keys()
sorted(data_dict.keys())
Struct = namedtuple('Struct', sorted(data_dict.keys()))
Struct._fields


# Of course we can still put in the correct values from the dictionary into the correct slots in the tuple by unpacking the dictionary instead of just the values:
d1 = Struct(**data_dict)
d1


# And of course, since this is now a named tuple we can access the data using the field name:
d1.complaint


# instead of how we would have done it with the dictionary:
data_dict['complaint']


# I also want to point out that with dictionaries we often end up with code where the key is stored in some variable and then referenced this way:
key_name = 'age'
data_dict[key_name]


# We cannot use this approach directly with named tuples however. For example this will not work:
key_name = 'age'
d1.key_name


# However, we can use the `getattr` function that we have seen before:
key_name = 'age'
getattr(d1, key_name)


# We also have the `get` method on dictionaries that can specify a default value to return if the key does not exist:
data_dict.get('age', None), data_dict.get('invalid_key', None)


# And we can do the same with the `getattr` function:
getattr(d1, 'age', None), getattr(d1, 'invalid_field', None)


# Now this is not very useful if you are only working with a single instance of a dictionary that has the same set of keys. Kind of pointless really.
# You also do not want to create a new named tuple for every instance of a dictionary - that would just be way too much overhead.
# But in cases where you have a collection of dictionaries that share a common set of keys, this can be really useful, as long as you are willing to live with the fact that you now have immutable structures.

# Let's suppose we have this data list:
data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]


# The first thing to note is that we need to figure out all the possible keys that have been used in the dictionaries in this list.

# The easiest way to do this is to extract all the keys of all the dictionaries and then make a `set` out of them, to eliminate duplicate key names:

# We could do it this way, using a simple loop:
keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)

keys


# But actually a more efficient way would be to use a comprehension:
keys = {key for dict_ in data_list for key in dict_.keys()}
keys


# In fact, we can also use the fact that we can union multiple sets (we'll cover this in detail later) by unpacking all the keys and creating a union of them:
keys = set().union(*(dict_.keys() for dict_ in data_list))
keys


# However you do it, we end up with a set of all the possible keys used in our list of dictionaries.

# Now we can go ahead and create a named tuple with all those keys as fields:
Struct = namedtuple('Struct', keys)
Struct._fields


# As you can see, sets do not preserve order, so in this case we'll probably sort the keys to create our named tuple:
Struct = namedtuple('Struct', sorted(keys))
Struct._fields


# Now, we're also going to provide default values, since not all dictionaries have all the keys in them. In this case I'm going to set the default to `None` if the key is missing:
Struct.__new__.__defaults__ = (None,) * len(Struct._fields)


# Now we're ready to load up all these dictionaries into a new list of named tuples:
tuple_list = [Struct(**dict_) for dict_ in data_list]
tuple_list


# So lastly, let's just package this all up neatly into a single function that will take an iterable of dictionaries, or an arbitrary number of dictionaries as positional arguments, and return a list of named tuples:
def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

tuplify_dicts(data_list)


# Isn't Python wonderful? :-)
