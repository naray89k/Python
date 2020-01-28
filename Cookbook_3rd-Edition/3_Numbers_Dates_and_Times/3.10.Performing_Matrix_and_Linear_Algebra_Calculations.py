#!/usr/bin/env python
# coding: utf-8
import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m

m.T

m.I

v = np.matrix([[2],[3],[4]])
v

m*v

import numpy.linalg
numpy.linalg.eigvals(m)

x = numpy.linalg.solve(m,v)
x

m*x

v



