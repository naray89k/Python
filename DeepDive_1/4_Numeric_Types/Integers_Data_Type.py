#!/usr/bin/env python
# coding: utf-8

# ## Integers

# Integers are objects - instances of the ``int`` class.
print(type(100))


# They are a variable length data type that can theoretically handle any integer magnitude. 
# This will take up a variable amount of memory that depends on the particular size of the integer.
import sys


# Creating an integer object requires an overhead of 24 bytes:
sys.getsizeof(0)


# Here we see that to store the number 1 required 4 bytes (32 bits) on top of the 24 byte overhead:
sys.getsizeof(1)


# Larger numbers will require more storage space:
sys.getsizeof(2**1000)


# Larger integers will also slow down calculations.
import time

def calc(a):
    for i in range(10000000):
        a * 2


# We start with a small integer value for a (10):
start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)


# Now we set a to something larger (2<sup>100</sup>):
start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end - start)


# Finally we set a to some really large value (2<sup>10,000</sup>):
start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)

