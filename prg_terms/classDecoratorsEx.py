#! /usr/bin/python

class decorator_class(object):
    def __init__(self,orig_func):
        self.orig_func=orig_func

    def __call__(self,*args,**kwargs):
        print 'call method executed this before {}'.format(self.orig_func.__name__)
        return self.orig_func(*args,**kwargs)

@decorator_class
def display():
    print "display Function Ran"


@decorator_class
def display_info(name,age):
    print 'display_info function ran with {} and {}'.format(name,age)


display()
display_info('John',25)
