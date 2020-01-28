#!/usr/bin/env python
# coding: utf-8
from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print (a+b)

print (a*b)

c = a*b
c.numerator

c.denominator

float(c)

print(c.limit_denominator(8))

x = 3.75
y = Fraction(*x.as_integer_ratio())
y



