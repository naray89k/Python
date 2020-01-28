#!/usr/bin/env python
# coding: utf-8
x = [1,2,3,4]
y = [5,6,7,8]
x * 2

x + 10

x + y 

import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])

ax*2

ax + 10

ax + ay

ax * ay

def f(x):
    return 3*x**2 - 2*x + 7

f(ax)

np.sqrt(ax)

np.cos(ax)

grid = np.zeros((10000,10000), dtype=float)

grid

grid += 10

grid

np.sin(grid)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a

a[1]

a[:,1]

a[1:3, 1:3]

a[1:3, 1:3] += 10

a

a + [100, 101, 102, 103]

a

np.where(a < 10, a, 10)

a

