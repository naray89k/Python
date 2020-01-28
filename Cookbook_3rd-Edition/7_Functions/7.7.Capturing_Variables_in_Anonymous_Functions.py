#!/usr/bin/env python
# coding: utf-8
x =10
a = lambda y:x+y

x=20

b= lambda y:x+y

a(10)

b(10)

x = 15
a(10)

x=3

a(10)

x=10
a = lambda y,x = x:x+y

x = 20

b = lambda y,x= x:x+y

a(10)

b(10)

funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))



