#!/usr/bin/env python
# coding: utf-8
import spam
import imp
imp.reload(spam)

# spam.py
def bar():
    print('bar')

def grok():
    print('grok')

import spam
from spam import grok
spam.bar()

grok()

def grok():
    print('New grok')

import imp
imp.reload(spam)

spam.bar()

grok()

spam.grok()

