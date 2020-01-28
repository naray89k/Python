#!/usr/bin/env python
# coding: utf-8
# setup.py
from distutils.core import setup, Extension

setup(name='ptexample',
      ext_modules=[
      Extension('ptexample',
      ['ptexample.c'],
      include_dirs = [], # May need pysample.h directory
               )
     ]
)

import sample
p1 = sample.Point(2,3)
p1

import ptexample
ptexample.print_point(p1)

