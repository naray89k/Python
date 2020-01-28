#!/usr/bin/env python
# coding: utf-8

# ### Complex Numbers

# Python's built-in class provides support for complex numbers.
# Complex numbers are defined in rectangular coordinates (real and imaginary parts) using either the constructor or a literal expression.

# The complex number 1 + 2j can be defined in either of these ways:
a = complex(1, 2)
b = 1 + 2j
a == b

# Note that the real and imaginary parts are defined as floats, and can be retrieved as follows:
a.real, type(a.real)
a.imag, type(a.imag)

# The complex conjugate can be calculated as follows:
a.conjugate()

# The standard arithmetic operatots are polymorphic and defined for complex numbers
a = 1 + 2j
b = 3 - 4j
c = 5j
d = 10
a + b
b * c
c / d
d - a

# The // and % operators, although also polymorphic, are not defined for complex numbers:
a // b
a % b

# The == and != operators support complex numbers - but since the real and imaginary parts of complex numbers are floats, the same problems comparing floats using == and != also apply to complex numbers.
a = 0.1j
a + a + a == 0.3j

# In addition, the standard comparison operators (<, <=, >, >=) are not defined for complex numbers.
a = 1 + 1j
b = 100 + 100j
a < b

# #### Math Functions

# The **cmath** module provides complex alternatives to the standard **math** functions.
# In addition, the **cmath** module provides the complex implementation of the **isclose()** method available for floats.
import cmath
a = 1 + 5j
print(cmath.sqrt(a))

# The standard **math** module functions will not work with complex numbers:
import math
print(math.sqrt(a))

# #### Polar / Rectangular Conversions

# The **cmath.phase()** function can be used to return the phase (or argument) of  any complex number.
# The standard **abs()** function supports complex numbers and will return the magnitude (euclidean norm) of the complex number.
a = 1 + 1j
r = abs(a)
phi = cmath.phase(a)
print('{0} = ({1},{2})'.format(a, r, phi))

# Complex numbers in polar coordinates can be converted to rectangular coordinates using the **math.rect()** function:
r = math.sqrt(2)
phi = cmath.pi/4
print(cmath.rect(r, phi))

# #### Euler's Identity and the **isclose()** function
# e<sup>i &pi;</sup> + 1 = 0
RHS = cmath.exp(cmath.pi * 1j) + 1
print(RHS)

# Which, because of limited precision is not quite zero.

# However, the result is very close to zero.
# We can use the **isclose()** method of the **cmath** module, which behaves similarly to the **math.isclose()** method. Since we are testing for closeness of two numbers close to zero, we need to make sure an absolute tolerance is also specified:
cmath.isclose(RHS, 0, abs_tol=0.00001)

# If we had not specified an absolute tolerance:
cmath.isclose(RHS, 0)

