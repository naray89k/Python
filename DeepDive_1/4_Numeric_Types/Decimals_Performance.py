#!/usr/bin/env python
# coding: utf-8

# ### Decimals: Performance Considerations
# #### Memory Footprint

# Decimals take up a lot more memory than floats.
import sys
from decimal import Decimal
a = 3.1415
b = Decimal('3.1415')
sys.getsizeof(a)

# 24 bytes are used to store the float 3.1415
sys.getsizeof(b)

# 104 bytes are used to store the Decimal 3.1415

# #### Computational Performance

# Decimal arithmetic is also much slower than float arithmetic (on a CPU, and even more so if using a GPU)
# We can do some rough timings to illustrate this.
# First we look at the performance difference creating floats vs decimals:
import time
from decimal import Decimal

def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')

# Timing float and Decimal operations:
n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

# We make a slight variant here to see how addition compares between the two types:
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

# How about square roots:
# (We drop the n count a bit)
n = 5000000

import math

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

