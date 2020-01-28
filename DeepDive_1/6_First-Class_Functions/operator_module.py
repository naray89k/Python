#!/usr/bin/env python
# coding: utf-8

# ### The **operator** Module
import operator

dir(operator)


# #### Arithmetic Operators

# A variety of arithmetic operators are implemented.
operator.add(1, 2)
operator.mul(2, 3)
operator.pow(2, 3)
operator.mod(13, 2)
operator.floordiv(13, 2)
operator.truediv(3, 2)


# These would have been very handy in our previous section:
from functools import reduce
reduce(lambda x, y: x*y, [1, 2, 3, 4])


# Instead of defining a lambda, we could simply use **operator.mul**:
reduce(operator.mul, [1, 2, 3, 4])

# #### Comparison and Boolean Operators

# Comparison and Boolean operators are also implemented as functions:
operator.lt(10, 100)
operator.le(10, 10)
operator.is_('abc', 'def')


# We can even get the truthyness of an object:
operator.truth([1,2])
operator.truth([])
operator.and_(True, False)
operator.or_(True, False)


# #### Element and Attribute Getters and Setters

# We generally select an item by index from a sequence by using **[n]**:
my_list = [1, 2, 3, 4]
my_list[1]


# We can do the same thing using:
operator.getitem(my_list, 1)


# If the sequence is mutable, we can also set or remove items:
my_list = [1, 2, 3, 4]
my_list[1] = 100
del my_list[3]
print(my_list)
my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
operator.delitem(my_list, 3)
print(my_list)


# We can also do the same thing using the **operator** module's **itemgetter** function.
# The difference is that this returns a callable:
f = operator.itemgetter(2)


# Now, **f(my_list)** will return **my_list[2]**
f(my_list)

x = 'python'
f(x)


# Furthermore, we can pass more than one index to **itemgetter**:
f = operator.itemgetter(2, 3)

my_list = [1, 2, 3, 4]
f(my_list)

x = 'pytyhon'
f(x)


# Similarly, **operator.attrgetter** does the same thing, but with object attributes.
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')

obj = MyClass()
obj.a, obj.b, obj.c
f = operator.attrgetter('a')
f(obj)
my_var = 'b'
operator.attrgetter(my_var)(obj)
my_var = 'c'
operator.attrgetter(my_var)(obj)
f = operator.attrgetter('a', 'b', 'c')
f(obj)


# Of course, attributes can also be methods.
# In this case, **attrgetter** will return the object's **test** method - a callable that can then be called using **()**:
f = operator.attrgetter('test')
obj_test_method = f(obj)
obj_test_method()


# Just like lambdas, we do not need to assign them to a variable name in order to use them:
operator.attrgetter('a', 'b')(obj)
operator.itemgetter(2, 3)('python')


# Of course, we can achieve the same thing using functions or lambdas:
f = lambda x: (x.a, x.b, x.c)
f(obj)
f = lambda x: (x[2], x[3])
f([1, 2, 3, 4])
f('python')


# ##### Use Case Example: Sorting

# Suppose we want to sort a list of complex numbers based on the real part of the numbers:
a = 2 + 5j
a.real
l = [10+1j, 8+2j, 5+3j]
sorted(l, key=operator.attrgetter('real'))


# Or if we want to sort a list of string based on the last character of the strings:
l = ['aaz', 'aad', 'aaa', 'aac']
sorted(l, key=operator.itemgetter(-1))


# Or maybe we want to sort a list of tuples based on the first item of each tuple:
l = [(2, 3, 4), (1, 2, 3), (4, ), (3, 4)]
sorted(l, key=operator.itemgetter(0))


# #### Slicing
l = [1, 2, 3, 4]
l[0:2]
l[0:2] = ['a', 'b', 'c']
print(l)
del l[3:5]
print(l)


# We can do the same thing this way:
l = [1, 2, 3, 4]
operator.getitem(l, slice(0,2))
operator.setitem(l, slice(0,2), ['a', 'b', 'c'])
print(l)
operator.delitem(l, slice(3, 5))
print(l)


# #### Calling another Callable
x = 'python'
x.upper()
operator.methodcaller('upper')('python')


# Of course, since **upper** is just an attribute of the string object **x**, we could also have used:
operator.attrgetter('upper')(x)()


# If the callable takes in more than one parameter, they can be specified as additional arguments in **methodcaller**:
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, c):
        print(self.a, self.b, c)

obj = MyClass()
obj.do_something(100)
operator.methodcaller('do_something', 100)(obj)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, *, c):
        print(self.a, self.b, c)

obj.do_something(c=100)
operator.methodcaller('do_something', c=100)(obj)


# More information on the **operator** module can be found here:
# https://docs.python.org/3/library/operator.html
