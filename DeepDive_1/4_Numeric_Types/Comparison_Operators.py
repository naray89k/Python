#!/usr/bin/env python
# coding: utf-8

# ### Comparison Operators
# #### Identity and Membership Operators
# The **is** and **is not** operators will work with any data type since they are comparing the memory addresses of the objects (which are integers)
0.1 is (3+4j)

'a' is [1, 2, 3]

# The **in** and **not in** operators are used with iterables and test membership:
1 in [1, 2, 3]

[1, 2] in [1, 2, 3]

[1, 2] in [[1,2], [2,3], 'abc']

'key1' in {'key1': 1, 'key2': 2}

1 in {'key1': 1, 'key2': 2}

# We'll come back to these operators in later sections on iterables and mappings.
# #### Equality Operators
# The **==** and **!=** operators are value comparison operators. 
# They will work with mixed types that are comparable in some sense.
# For example, you can compare Fraction and Decimal objects, but it would not make sense to compare string and integer objects.
1 == '1'

from decimal import Decimal
from fractions import Fraction

Decimal('0.1') == Fraction(1, 10)

1 == 1 + 0j

True == Fraction(2, 2)

False == 0j

# #### Ordering Comparisons
# Many, but not all data types have an ordering defined.
# For example, complex numbers do not.
1 + 1j < 2 + 2j

# Mixed type ordering comparisons is supported, but again, it needs to make sense:
1 < 'a'

Decimal('0.1') < Fraction(1, 2)

# #### Chained Comparisons
# It is possible to chain comparisons.
# For example, in **a < b < c**, Python simply **ands** the pairwise comparisons: **a < b and b < c**
1 < 2 < 3

1 < 2 > -5 < 50 > 4

1 < 2 == Decimal('2.0')

import string
'A' < 'a' < 'z' > 'Z' in string.ascii_letters

