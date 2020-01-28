#!/usr/bin/env python
# coding: utf-8
import logging
a = logging.getLogger('foo')
b = logging.getLogger('bar')
a is b

c = logging.getLogger('foo')

a is c

# The class in question
class Spam:
    def __init__(self, name):
        self.name = name

# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

a= get_spam('foo')

b = get_spam('bar')

a is b

c = get_spam('foo')

a is c

# Note: This code doesn't quite work
import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
        return self
 
    def __init__(self, name):
        print('Initializing Spam')
        self.name = name

s = Spam('Dave')

t = Spam('Dave')

s is t 

a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
list(_spam_cache)

del a
del c
list(_spam_cache)

del b
list(_spam_cache)

import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
 
    def clear(self):
        self._cache.clear()

        
class Spam:
    manager = CachedSpamManager()
    def __init__(self, name):
        self.name = name

def get_spam(name):
    return Spam.manager.get_spam(name)

a = Spam('foo')
b = Spam('foo')
a is b

class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")
 
    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name

import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name) # Modified creation
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

