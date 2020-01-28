#!/usr/bin/env python
# coding: utf-8

# ### The For Loop

# An **iterable** is something can be iterated over. :-)

# Maybe a better non-circular way to define iterable is to think of it as a collection of things that can be accessed one at a time.
# In Python, an **iterable** has a very specific meaning: an iterable is an **object** capable of returning its members one at a time.
# Many objects in Python are iterable: lists, strings, file objects and many more.
# The **for** keyword can be used to iterate an iterable.

# iterating over a range of elements
for i in range(5):
    print(i)

# Equivalent logic in while loop
i = 0
while i < 5:
    #code block
    print(i)
    i += 1
i = None

# Iterating over a list of elements.
for x in [1, 2, 3]:
    print(x)

# Iterating over a sequence of characters(string).
for x in 'hello':
    print(x)

# Iterating over a tuple of elements.
for x in ('a', 'b', 'c'):
    print(x)

# Iterating over a tuple of elements.
for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

# We can even assign the individual tuple values to specific named variables:
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)


# The **break** and **continue** statements work just as well in **for** loops as they do in **where** loops:
for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)


# The **for** loop, like the **while** loop, also supports an **else** clause which is executed if and only if the loop terminates normally (i.e. did not exit because of a **break** statement)
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')


for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')


# Similarly to the **where** loop, **break** and **continue** work just the same in the context of a **try** statement's **finally** clause.
for i in range(5):
    print('--------------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always runs')
    print(i)


# There are a number of standard techniques to iterate over iterables:
s = 'hello'
for c in s:
    print(c)


# But sometimes, for indexable iterable types (e.g. sequences), we want to also know the index of the item in the loop:
s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1


# Slightly better approach might be:
s = 'hello'
for i in range(len(s)):
    print(i, s[i])


# or even better:
s = 'hello'
for i, c in enumerate(s):
    print(i, c)

