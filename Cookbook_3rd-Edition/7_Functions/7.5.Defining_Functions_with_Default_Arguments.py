#!/usr/bin/env python
# coding: utf-8
def spam(a, b=42):
    print(a,b)

spam(1)

spam(1,2)

def spam(a, b=None):
    if b is None:
        b = []

_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

spam(1)

spam(1,2)

spam(1, None)

x = 42
def spam(a, b=x):
    print(a,b)

spam(1)

x = 23

spam(1)

def spam(a, b=[]):

def spam(a, b=[]):
    print(b)
    return(b)

x = spam(1)

x.append(99)

x.append('Yow!')

x

spam(1)

def spam(a, b=None):
    if not b:
        b = []

spam(1)

x=[]

spam(1,x)

spam(1,0)

spam(1,'')



