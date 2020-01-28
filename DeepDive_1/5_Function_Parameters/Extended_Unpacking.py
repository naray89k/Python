#!/usr/bin/env python
# coding: utf-8

# ### Extended Unpacking

# Let's see how we might split a list into it's first element, and "everything else" using slicing:
l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]
print(a)
print(b)


# We can even use unpacking to simplify this slightly:
a, b = l[0], l[1:]
print(a)
print(b)


# But we can use the **\*** operator to achieve the same result:
a, *b = l
print(a)
print(b)


# Note that the **\*** operator can only appear **once**!

# Like standard unpacking, this extended unpacking will work with any iterable.
# With tuples:
a, *b = -10, 5, 2, 100
print(a)
print(b)


# With strings:
a, *b = 'python'
print(a)
print(b)


# What about extracting the first, second, last elements and *the rest*.
# Again we can use slicing:
s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)


# But we can just as easily do it this way using unpacking:
a, b, *c, d = s
print(a)
print(b)
print(c)
print(d)


# As you can see though, **c** is a list of characters, not a string.
# It that's a problem we can easily fix it this way:
print(c)
c = ''.join(c)
print(c)


# We can also use unpacking on the right hand side of an assignment expression:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
s = 'ABC'
l = [*l1, *s]
print(l)


# This unpacking works with unordered types such as sets and dictionaries as well.
# The only thing is that it may not be very useful considering there is no particular ordering, so a first or last element has no real useful meaning.
s = {10, -99, 3, 'd'}

for c in s:
    print(c)


# As you can see, the order of the elements when we created the set was not retained!
s = {10, -99, 3, 'd'}
a, b, *c = s
print(a)
print(b)
print(c)


# So unpacking this way is of limited use.
# However consider this:
s = {10, -99, 3, 'd'}
*a, = s
print(a)


# At first blush, this doesn't look terribly exciting - we simply unpacked the set values into a list.
# But this is actually quite useful in both sets and dictionaries to combine things (although to be sure, there are alternative ways to do this as well - which we'll cover later in this course)
s1 = {1, 2, 3}
s2 = {3, 4, 5}


# How can we combine both these sets into a single merged set?
s1 + s2


# Well, **+** doesn't work...

# We could use the built-in method for unioning sets:
help(set)
print(s1)
print(s2)
s1.union(s2)


# What about joining 4 different sets?
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2, s3, s4))


# Or we could use unpacking in this way:
{*s1, *s2, *s3, *s4}


# What we did here was to unpack each set directly into another set!

# The same works for dictionaries - just remember that **\*** for dictionaries unpacks the keys only.
d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}
[*d1, *d2]


# So, is there anything to unpack the key-value pairs for dictionaries instead of just the keys?

# Yes - we can use the **\*\*** operator:
d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}

{**d1, **d2}


# Notice what happened to the value of **key2**. The value for the second occurrence of **key2** was retained (overwritten).

# In fact, if we write the unpacking reversing the order of d1 and d2:
{**d2, **d1}


# we see that the value of **key2** is now **2**, since it was the second occurrence.

# Of course, we can unpack a dictionary into a dictionary as seen above, but we can mix in our own key-value pairs as well - it is just a dictionary literal after all.
{'a': 1, 'b': 2, **d1, **d2, 'c':3}


# Again, if we have the same keys, only the "latest" value of the key is retained:
{'key1': 100, **d1, **d2, 'key3': 200}


# #### Nested Unpacking

# Python even supports nested unpacking:
a, b, (c, d) = [1, 2, ['X', 'Y']]
print(a)
print(b)
print(c)
print(d)


# In fact, since a string is an iterable, we can even write:
a, b, (c, d) = [1, 2, 'XY']
print(a)
print(b)
print(c)
print(d)


# We can even write something like this:
a, b, (c, d, *e) = [1, 2, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)


# Remember when we said that we can use a * only **once**...

# How about this then?
a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)


# We can break down what happened here in multiple steps:
a, *b, tmp = [1, 2, 3, 'python']
print(a)
print(b)
print(tmp)

c, d, *e = tmp
print(c)
print(d)
print(e)


# So putting it together we get our original line of code:
a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)


# If we wanted to do the same thing using slicing:
l = [1, 2, 3, 'python']
l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])

l = [1, 2, 3, 'python']
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)


# Of course, this works for arbitrary lengths and indexable sequence types:
l = [1, 2, 3, 4, 'unladen swallow']
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)


# or even:
l = [1, 2, 3, 4, ['a', 'b', 'c', 'd']]
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
