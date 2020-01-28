#!/usr/bin/env python
# coding: utf-8

# ### Challenge: Randomizing an Iterable using Sorted
import random
help(random.random)
random.random()
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted(l, key=lambda x: random.random())


# Of course, this works for any iterable:
sorted('abcdefg', key = lambda x: random.random())


# And to get a string back instead of just a list:
''.join(sorted('abcdefg', key = lambda x: random.random()))
