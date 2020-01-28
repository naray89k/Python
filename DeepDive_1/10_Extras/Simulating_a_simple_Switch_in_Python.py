#!/usr/bin/env python
# coding: utf-8

# ### Simulating a simple Switch in Python

# This is based on a few questions I've received regarding a `switch` statement in Python.
# Python does not have a switch statement, but it is possible to have similar functionality in a variety of ways.
# Here I'm going to assume a simple `switch` statement where each `case` has a `break` (in other words, no fall through), and is based on a single value.
# You can see a PEP that discussed adding a `switch` statement to Python, proposed by Guido, but ultimately rejected (by Guido as well):
# https://www.python.org/dev/peps/pep-3103/

# A simple Java example would be something like this:

# ```
# switch (dow) {
#     case 1: dowString = 'Monday';
#             break;
#     case 2: dowString = 'Tuesday';
#             break;
#     case 3: dowString = 'Wednesday';
#             break;
#     case 4: dowString = 'Thursday';
#             break;
#     case 5: dowString = 'Friday';
#             break;
#     case 6: dowString = 'Saturday';
#             break;
#     case 7: dowString = 'Sunday';
#             break;
#     default: dowString = 'Invalid day of week';
# }
# ```

# The simplest approach here is to simply use an `if...elif...else` structure.
# To make it slightly more interesting, I'm not going to set a variable for each case statement, I'm going to return a function - to keep it simple I'll just call the `print()` function, but it could be anything really.
def dow_switch_fn(dow):
    if dow == 1:
        fn = lambda: print('Monday')
    elif dow == 2:
        fn = lambda: print('Tuesday')
    elif dow == 3:
        fn = lambda: print('Wednesday')
    elif dow == 4:
        fn = lambda: print('Thursday')
    elif dow == 5:
        fn = lambda: print('Friday')
    elif dow == 6:
        fn = lambda: print('Saturday')
    elif dow == 7:
        fn = lambda: print('Sunday')
    else:
        fn = lambda: print('Invalid day of week')
    
    return fn()

dow_switch_fn(1)

dow_switch_fn(100)


# Now, dictionaries could also be used quite effectively here:
def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }
    
    return dow_dict.get(dow, dow_dict['default'])()

dow_switch_dict(1)

dow_switch_dict(100)


# One advantage of using a dictionary (as an associative array), is that you can add and remove elements from the dictionary at run time. Of course you cannot do that with the `if...elif...else` - you need to know at compile time how many branches your "switch" has (just like a regular `switch` would, that is also fixed once the code has been compiled+
# ).
# But the downside of this approach compared to `if...elif...else` is that the dictionary values are relatively simple and cannot contain nested if statements or anything else. In the case of `if...elif...else` your code blocks for each of these statement can contain as many lines of code as you want.
# So the choice is yours, and depends on what you are trying to accomplish.
# Now, there is also another way to do this, and it is based on the concepts I discuss in the decorator videos on the single dispatch generic functions.
# We cannot use the standard library's `@singledispatch` decorator, but we can adapt the approach I showed you to create a `switch` function where we can register each `case` of the `switch`.
# First, let's recall our own implementation of the `@singledispatch` decorator:
def singledispatch(fn):
    registry = dict()
    registry[object] = fn
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner
   
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    decorator.register = register
    return decorator


# With this decorator, we are dispatching based on the type. But if you think of our `switch` statement, we really just want to dispatch based on a value (like the `dow` value).
# So let's tweak the decorator to no longer use a type, but an arbitrary value instead:
def switcher(fn):
    registry = dict()
    registry['default'] = fn
    
    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn  # we do this so we can stack register decorators!
        return inner
   
    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()

    decorator.register = register
    return decorator


# And that's all we need to change!

# We can now use it as follows:
@switcher
def dow():
    print('Invalid day of week')
    
@dow.register(1)
def dow_1():
    print('Monday')
    
dow.register(2)(lambda: print('Tuesday'))
dow.register(3)(lambda: print('Wednesday'))
dow.register(4)(lambda: print('Thursday'))
dow.register(5)(lambda: print('Friday'))
dow.register(6)(lambda: print('Saturday'))
dow.register(7)(lambda: print('Sunday'))


# And we can now use it this way:
dow(1)

dow(2)

dow(100)


# Of course you'll notice that our decorator is simply using the same dictionary / associative array approach we just looked at - except we can use decorators to do that work.


