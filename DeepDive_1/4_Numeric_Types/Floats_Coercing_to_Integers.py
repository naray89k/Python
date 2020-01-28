#!/usr/bin/env python
# coding: utf-8

# ### Coercing Floats to Integers

# #### Truncation
from math import trunc
trunc(10.3), trunc(10.5), trunc(10.6)
trunc(-10.6), trunc(-10.5), trunc(-10.3)


# The **int** constructor uses truncation when a float is passed in:
int(10.3), int(10.5), int(10.6)
int(-10.5), int(-10.5), int(-10.4)


# #### Floor
from math import floor
floor(10.4), floor(10.5), floor(10.6)
floor(-10.4), floor(-10.5), floor(-10.6)


# #### Ceiling
from math import ceil
ceil(10.4), ceil(10.5), ceil(10.6)
ceil(-10.4), ceil(-10.5), ceil(-10.6)
