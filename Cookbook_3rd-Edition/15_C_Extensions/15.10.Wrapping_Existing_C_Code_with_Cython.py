#!/usr/bin/env python
# coding: utf-8
# sample.pyx

# Import the low-level C declarations
cimport csample

# Import some functionality from Python and the C stdlib
from cpython.pycapsule cimport *

from libc.stdlib cimport malloc, free

# Wrappers
def gcd(unsigned int x, unsigned int y):
    return csample.gcd(x, y)

def in_mandel(x, y, unsigned int n):
    return csample.in_mandel(x, y, n)

def divide(x, y):
    cdef int rem
    quot = csample.divide(x, y, &rem)
    return quot, rem

def avg(double[:] a):
    cdef:
        int sz
        double result
 
    sz = a.size
    with nogil:
        result = csample.avg(<double *> &a[0], sz)
    return result

# Destructor for cleaning up Point objects
cdef del_Point(object obj):
    pt = <csample.Point *> PyCapsule_GetPointer(obj,"Point")
    free(<void *> pt)

# Create a Point object and return as a capsule
def Point(double x,double y):
    cdef csample.Point *p
    p = <csample.Point *> malloc(sizeof(csample.Point))
    if p == NULL:
        raise MemoryError("No memory to make a Point")
    p.x = x
    p.y = y
    return PyCapsule_New(<void *>p,"Point",<PyCapsule_Destructor>del_Point)

def distance(p1, p2):
    pt1 = <csample.Point *> PyCapsule_GetPointer(p1,"Point")
    pt2 = <csample.Point *> PyCapsule_GetPointer(p2,"Point")
    return csample.distance(pt1,pt2)

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension('sample',
              ['sample.pyx'],
            libraries=['sample'],
            library_dirs=['.'])]

setup(
    name = 'Sample extension module',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

import sample
sample.gcd(42,10)

sample.in_mandel(1,1,400)

sample.in_mandel(0,0,400)

sample.divide(42,10)

import array
a = array.array('d',[1,2,3])
sample.avg(a)

p1 = sample.Point(2,3)
p2 = sample.Point(4,5)
p1

p2

sample.distance(p1,p2)

cimport csample

def gcd(unsigned int x, unsigned int y):
    return csample.gcd(x,y)

def gcd(unsigned int x, unsigned int y):
    if x <= 0:
        raise ValueError("x must be > 0")
    if y <= 0:
        raise ValueError("y must be > 0")
    return csample.gcd(x,y)

def divide(x,y):
    cdef int rem
    quot = csample.divide(x,y,&rem)
    return quot, rem

import array
a = array.array('d',[1,2,3])
import numpy
b = numpy.array([1., 2., 3.])
import sample
sample.avg(a)
sample.avg(b

from cpython.pycapsule cimport *
from libc.stdlib cimport malloc, free

# sample.pyx

cimport csample
from libc.stdlib cimport malloc, free

cdef class Point:
    cdef csample.Point *_c_point
    def __cinit__(self, double x, double y):
        self._c_point = <csample.Point *> malloc(sizeof(csample.Point))
        self._c_point.x = x
        self._c_point.y = y
 
    def __dealloc__(self):
        free(self._c_point)
        
    property x:
        def __get__(self):
            return self._c_point.x
 
        def __set__(self, value):
            self._c_point.x = value
 
    property y:
        def __get__(self):
            return self._c_point.y
        def __set__(self, value):
            self._c_point.y = value
    
    def distance(Point p1, Point p2):
        return csample.distance(p1._c_point, p2._c_point)

import sample
p1 = sample.Point(2,3)
p2 = sample.Point(4,5)
p1

p2

p1.x

p1.y

sample.distance(p1,p2)

