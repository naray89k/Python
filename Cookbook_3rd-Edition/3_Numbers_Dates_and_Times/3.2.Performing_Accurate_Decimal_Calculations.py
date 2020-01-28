#!/usr/bin/env python
# coding: utf-8
a = 4.2
b = 2.1
a + b

(a+b) == 6.3

from decimal import Decimal 

a = Decimal('4.2')
b = Decimal('2.1')

a+b

(a+b) == Decimal('6.3')

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

nums = [1.23e+18, 1, -1.23e+18]
sum(nums)

import math
math.fsum(nums)



