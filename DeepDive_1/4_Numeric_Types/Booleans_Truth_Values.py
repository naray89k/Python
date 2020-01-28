#!/usr/bin/env python
# coding: utf-8

# ### Booleans: Truth Values
# All objects in Python have an associated **truth value**, or **truthyness**
# We saw in a previous lecture that integers have an inherent truth value:
bool(0)
bool(1), bool(-1), bool(100)

# This truthyness has nothing to do with the fact that **bool** is a subclass of **int**.
# Instead, it has to do with the fact that the **int** class implements a `__bool__()` method:
help(bool)

# If you scroll down in the documentation you shoudl reach a section that looks like this:
# `` 
# |  __bool__(self, /)
# |      self != 0
# ``

# So, when we write:
bool(100)

# Python is actually calling 100.__bool__() and returning that:
(100).__bool__()

(0).__bool__()

# Most objects will implement either the `__bool__()` or `__len__()` methods. If they don't, then their associated value will be **True** always.
# #### Numeric Types
# Any non-zero numeric value is truthy. Any zero numeric value is falsy:
from fractions import Fraction
from decimal import Decimal
bool(10), bool(1.5), bool(Fraction(3, 4)), bool(Decimal('10.5'))

bool(0), bool(0.0), bool(Fraction(0,1)), bool(Decimal('0')), bool(0j)

# #### Sequence Types
# An empty sequence type object is Falsy, a non-empty one is truthy:
bool([1, 2, 3]), bool((1, 2, 3)), bool('abc'), bool(1j)

bool([]), bool(()), bool('')

# #### Mapping Types

# Similarly, an empty mapping type will be falsy, a non-empty one truthy:
bool({'a': 1}), bool({1, 2, 3})

bool({}), bool(set())

# #### The None Object

# The singleton **None** object is always falsy:
bool(None)

# #### One Application of Truth Values

# Any conditional expression which involves objects other than **bool** types, will use the associated truth value as the result of the conditional expression.
a = [1, 2, 3]
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = []
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = 'abc'
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = ''
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

# We could write this using a more lengthy expression:
a = 'abc'
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('a is None, or a is empty')

# Doing the following would break our code in some instances:
a = 'abc'
if a is not None:
    print(a[0])

# works, but:
a = ''
if a is not None:
    print(a[0])

a = None
if len(a) > 0:
    print(a[0])

# To be torough we would need to write:
a = None
if a is not None and len(a) > 0:
    print(a[0])

# Also, the order of the boolean expressions matter here!
# We'll discuss this and short-circuit evaluations in an upcoming video.
# For example:
a = None
if len(a) > 0 and a is not None:
    print(a[0])

