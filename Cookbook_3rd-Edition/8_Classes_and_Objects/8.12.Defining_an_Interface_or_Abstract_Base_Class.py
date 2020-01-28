#!/usr/bin/env python
# coding: utf-8
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

a = IStream() 

class SocketStream(IStream):
    def read(self, maxbytes=-1):
 
    def write(self, data):

def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')

import io

# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)

# Open a normal file and type check
f = open('foo.txt')
isinstance(f, IStream) 

from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass
 
    
    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    
    @classmethod
    @abstractmethod
    def method1(cls):
        pass


    @staticmethod
    @abstractmethod
    def method2():
        pass

import collections
# Check if x is a sequence
if isinstance(x, collections.Sequence):
 
# Check if x is iterable
if isinstance(x, collections.Iterable):

# Check if x has a size
if isinstance(x, collections.Sized):

# Check if x is a mapping
if isinstance(x, collections.Mapping):

from decimal import Decimal
import numbers

x = Decimal('3.4')
isinstance(x, numbers.Real) 

