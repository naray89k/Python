#!/usr/bin/env python
# coding: utf-8

# ### Sentinel Values for Parameter Defaults

# Often we specify the default for a function parameter as `None`. This allows to determine if the user specified an argument for that parameter or not. 
# There's a potential issue here!
# What happens if we need to differentiate between the following:
# * a non-`None` value was provided for the argument
# * a `None` value *was* provided for the argument
# * the argument was not provided at all

# Obviously, if we write our function this way, it will not work as intended:
def validate(a=None):
    if a is not None:
       print('Argument was provided')
    else:
        print('Argument was not provided')

validate(100)

validate()

validate(None)


# Instead, we need to use a different **sentinel** value. But which one?
# How can we **guarantee** that whatever sentinel we use will not be explicitly passed in by the user?

# For example we could try to use something like an unlikely string or integer. But that does not guarantee that the caller won't use that precise sentinel value at some point.

# The easiest thing to do is to create an instance of the `object` class. This is guaranteed to result in an object that the user cannot pass to us (they have no way of getting their hands on that object - or at least not without the absolute intention to do so). (remember that Python will always allow us to shoot ourselves in the foot if we try hard enough :-) )
_sentinel = object()

def validate(a=_sentinel):
    if a is not _sentinel:
        print('Argument was provided')
    else:
        print('Argument was not provided')

validate(100)

validate(None)

validate()

validate(object())


# Now, instead of using a separate variable to hold the sentinel value (`_sentinel`), we can introspect the function to find out what the default sentinel value is:
def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('Argument was provided')
    else:
        print('Argument was not provided')
    
    

validate(100)

validate(None)

validate()

validate(object())


# We can expand this to several parameters as well if we need to, using either method:
def validate(a=object(), b=object(), *, kw=object()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_kw = validate.__kwdefaults__['kw']
    
    if a is not default_a:
        print('Argument a was provided')
    else:
        print('Argument a was not provided')
        
    if b is not default_b:
        print('Argument b was provided')
    else:
        print('Argument b was not provided')
        
    if kw is not default_kw:
        print('Argument kw was provided')
    else:
        print('Argument kw was not provided')

validate(100, 200, kw=None)

validate(100, 200)

validate(b=100)

validate()



