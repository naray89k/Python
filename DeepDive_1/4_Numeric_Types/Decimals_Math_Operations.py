#!/usr/bin/env python
# coding: utf-8

# ### Decimals - Math Operations

# #### Div and Mod

# The // and % operators (and consequently, the divmod() function) behave differently for integers and Decimals.
# This is because integer division for Decimals is performed differently, 
# and results in a truncated division, whereas integers use a floored division.
# These differences are only when negative numbers are involved. 
# If all numbers involved are positive, then integer and Decimal div and mod operations are equal.
# But in both cases the // and % operators satisfy the equation:
# ``n = d * (n // d) + (n % d)``
import decimal
from decimal import Decimal

x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + x % y)

a = Decimal('10')
b = Decimal('3')
print(a//b, a%b)
print(divmod(a, b))
print( a == b * (a//b) + a % b)


# As we can see, the // and % operators had the same result when both numbers were positive.
x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + x % y)

a = Decimal('-10')
b = Decimal('3')
print(a//b, a%b)
print(divmod(a, b))
print( a == b * (a//b) + a % b)


# On the other hand, we see that in this case the // and % operators did not result in the same values, although the equation was satisfied in both instances.

# #### Other Mathematical Functions

# The Decimal class implements a variety of mathematical functions.
a = Decimal('1.5')
print(a.log10())  # base 10 logarithm
print(a.ln())     # natural logarithm (base e)
print(a.exp())    # e**a
print(a.sqrt())   # square root


# Although you can use the math function of the math module, be aware that the math module functions will cast the Decimal numbers to floats when it performs the various operations. So, if the precision is important (which it probably is if you decided to use Decimal numbers in the first place), choose the math functions of the Decimal class over those of the math module.
x = 2
x_dec = Decimal(2)

import math

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

x = 0.01
x_dec = Decimal('0.01')

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

