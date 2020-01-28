#!/usr/bin/env python
# coding: utf-8

# ### Rounding
help(round)


# #### n = 0
a = round(1.5)
a, type(a)

a = round(1.5, 0)
a, type(b)


# #### n > 0
round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0)


# #### n < 0
round(888.88, 1), round(888.88, 0), round(888.88, -1), round(888.88, -2), round(888.88, -3)


# #### Ties
round(1.25, 1)
round(1.35, 1)


# This is rounding to nearest, with ties to nearest number with even least significant digit, aka Banker's Rounding.

# Works similarly with **n** negative.
round(15, -1)
round(25, -1)


# #### Rounding to closest, ties away from zero

# This is traditionally the type of rounding taught in school, which is different from the Banker's Rounding implemented in Python (and in many other programming languages)

# 1.5 --> 2 <br>
# 2.5 --> 3 <br>
# -1.5 --> -2 <br>
# -2.5 --> -3 <br>

# To do this type of rounding (to nearest 1) we can add (for positive numbers) or subtract (for negative numbers) 0.5 and then truncate the resulting number.
def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

round(1.5), _round(1.5)
round(2.5), _round(2.5)

