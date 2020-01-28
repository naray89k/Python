#!/usr/bin/env python
# coding: utf-8
# setup.py
from distutils.core import setup, Extension

setup(name='sample',
    py_modules=['sample.py'],
    ext_modules=[
     Extension('_sample',
                 ['sample_wrap.c'],
                 include_dirs = [],
                 define_macros = [],
                 undef_macros = [],
                 library_dirs = [],
                 libraries = ['sample']
                 )
         ]
)

import sample
sample.gcd(42,8)

sample.divide(42,8)

p1 = sample.Point(2,3)
p2 = sample.Point(4,5)
sample.distance(p1,p2)

p1.x

p1.y

import array
a = array.array('d',[1,2,3])
sample.avg(a)

p1 = sample.Point(2,3)
# Usage if %extend Point is omitted
p1 = sample.Point()
p1.x = 2.0
p1.y = 3
sample.divide(42,8)

