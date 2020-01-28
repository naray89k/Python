#!/usr/bin/env python
# coding: utf-8

# ### Higher-Order Functions: Map and Filter

# **Definition**: A function that takes a function as an argument, and/or returns a function as its return value

# For example, the **sorted** function is a higher-order function as we saw in an earlier video.

# #### Map

# The **map** built-in function is a higher-order function that applies a function to an iterable type object:
help(map)

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

fact(3)
fact(4)
map(fact, [1, 2, 3, 4, 5])


# The **map** function returns a **map** object, which is an **iterable** - we can either convert that to a list or enumerate it:
l = list(map(fact, [1, 2, 3, 4, 5]))
print(l)


# We can also use it this way:
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
f = lambda x, y: x+y
m = map(f, l1, l2)
list(m)


# #### Filter
help(filter)


# The **filter** function is a function that filters an iterable based on the truthyness of the elements, or the truthyness of the elements after applying a function to them. Like the **map** function, the **filter** function returns an iterable that we can view by generating a list from it, or simply enumerating in a for loop.
l = [0, 1, 2, 3, 4, 5, 6]
for e in filter(None, l):
    print(e)


# Notice how **0** was eliminated from the list, since **0** is **falsy**.
# We can use a function for this filtering.
# Suppose we want to filter out all odd values, only retaining even values:

# We could first define a function to return True if the value is even, and False otherwise:
def is_even(n):
    return n % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))


# Of course, we could just use a lambda expression instead:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))


# #### Alternatives to **map** and **filter** using Comprehensions

# We'll cover comprehensions in much more detail later, but, for now, just be aware that we can use comprehensions instead of the **map** and **filter** functions - you decide which one you find more readable and enjoyable to write.

# ##### Map using a list comprehension:
# * factorial example
l = [1, 2, 3, 4, 5]
result = [fact(i) for i in l]
print(result)


# * two iterables example
# Before we do this example we need to know about the **zip** function.
# The **zip** built-in function will take one or more iterables, and generate an iterable of tuples where each tuple contains one element from each iterable:
l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
list(zip(l1, l2))

l1 = 1, 2, 3
l2 = [10, 20, 30]
l3 = ('a', 'b', 'c')
list(zip(l1, l2, l3))

l1 = [1, 2, 3]
l2 = (10, 20, 30)
l3 = 'abc'
list(zip(l1, l2, l3))

l1 = range(100)
l2 = 'python'
list(zip(l1, l2))


# Using the **zip** function we can now add our two lists element by element as follows:
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i,j in zip(l1,l2)]
print(result)


# ##### Filtering using a comprehension

# We can very easily filter an iterable using a comprehension as follows:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [i for i in l if i % 2 == 0]
print(result)


# As you can see, we did not even need a lambda expression!

# #### Combining **map** and **filter**
list(filter(lambda y: y < 25, map(lambda x: x**2, range(10))))


# Alternatively, we can use a list comprehension to do the same thing:
[x**2 for x in range(10) if x**2 < 25]


# We will come back, in more detail, to comprehensions and generators later in this course.
