#!/usr/bin/env python
# coding: utf-8
# setup.py
from distutils.core import setup, Extension

setup(name='sample',
        ext_modules=[
        Extension('sample',
        ['pysample.c'],
        include_dirs = ['/some/dir'],
        define_macros = [('FOO','1')],
        undef_macros = ['BAR'],
        library_dirs = ['/usr/local/lib'],
        libraries = ['sample']
        )
    ]
)

import sample
sample.gcd(35, 42)

sample.in_mandel(0, 0, 500)

sample.in_mandel(2.0, 1.0, 500)

sample.divide(42, 8)



