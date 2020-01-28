#!/usr/bin/env python
# coding: utf-8
import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)

countdown.__name__

countdown.__doc__

countdown.__annotations__

countdown.__name__

countdown.__doc__
countdown.__annotations__

countdown.__wrapped__(100000)

from inspect import signature
print(signature(countdown))



