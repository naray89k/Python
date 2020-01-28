#! /usr/bin/python
import time
from functools import wraps

def decorator_func(orig_func):
    def wrapper_func(*args,**kwargs):
        print('Executed the wrapper_func before {}'.format(orig_func.__name__))
        return orig_func(*args,**kwargs)
    return wrapper_func

@decorator_func
def display():
    print("display Function Ran")


@decorator_func
def display_info(name,age):
    print('display_info function ran with {} and {}'.format(name,age))


#decorated_display = decorator_func(display)
#decorated_display()
display()
display_info('John',25)

#The Above code is ordinary decorator

# ========= PRACTICAL EXAMPLE =============
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args,**kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=orig_func(*args,**kwargs)
        t2=time.time()-t1
        print('{} : Ran in {}'.format(orig_func.__name__,t2))
        return result

    return wrapper

@my_logger
@my_timer
def display_info(*args,**kwargs):
    time.sleep(1)
    print('display_info function ran with {},{}'.format(args,kwargs))


@my_timer
def display_info_timer(*args,**kwargs):
    time.sleep(1)
    print('display_info function ran with {},{}'.format(args,kwargs))


#display_info_logger('Narayanan',34)
#display_info_logger('Gandhimathi',26)
#display_info_logger('Gandhimathi',26,Graduation="BE")
display_info('Gandhimathi',26,Graduation="BE")
