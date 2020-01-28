#!/usr/bin/env python
# coding: utf-8

# ### Loop Break and Continue inside a Try...Except...Finally
# Recall that in a ``try`` statement, the ``finally`` clause always runs:
a = 10
b = 1
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')

# -----------------
a = 10
b = 0
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')

# -----------------

# So, what happens when using a ``try`` statement within a ``while`` loop, and a ``continue`` or ``break`` statement is encountered?
a = 0
b = 2
while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        continue
    finally:
        print('{0}, {1} - always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))

# -----------------

# As you can see in the above result, the ``finally`` code still executed, 
# even though the current iteration was cut short with the ``continue`` statement. 
# This works the same with a ``break`` statement:

a = 0
b = 2
while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))

# -----------------

# We can even combine all this with the ``else`` clause:
a = 0
b = 2
while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')

# -----------------

a = 0
b = 5
while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')

# -----------------

