#!/usr/bin/env python
# coding: utf-8
bash % env PYTHONPATH=/some/dir:/other/dir python3
Python 3.3.0 (default, Oct 4 2012, 10:17:33)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin

import sys
sys.path

import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(dirname('__file__'), 'src'))

