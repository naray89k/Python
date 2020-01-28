#!/usr/bin/env python
# coding: utf-8

# ### Named Tuples

# The ``namedtuple`` function in ``collections`` allows us to create a tuple that also has names attached to each field (aka property). This can be handy to reference data in the tuple structure by name instead of just relying on position.
# The ``namedtuple`` function is basically a class factory that creates a new type of class that uses a tuple as its underlying data storage (in fact, named tuples inherit from `tuple`), but layers in field names to each position and makes a property out of the field name.
# The ``namedtuple`` function creates a **class**, and we then use that class to instantiate our instances of named tuples.

# To use the ``namedtuple`` function we therefore need to select a class **name**, as well as indicate the **property** names, in the order in which they will be stored and accessed in the tuple.
# Note that a ``namedtuple``, like the regular ``tuple`` is an **immutable** data structure. (In fact, named tuples inherit from tuples - we'll revisit this in our section on metaclasses)

# If you find yourself writing code such as:
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Forget it! You seriously need to use named tuples! Not only can you shorten the amount of code you need to write, but you get some additional functionality for "free", such as `__repr__` and `__eq__` that you do not have to implement yourself!

# #### Creating Named Tuples

# We are going to create a ``Point`` named tuple that will contain an x-coordinate and a y-coordinate.
from collections import namedtuple
Point2D = namedtuple('Point2D', ('x', 'y'))


# Note that we have two different uses of `Point2D` here. The label we are assigning the return value of the call to ``namedtuple`` and the **name** of the class generated by calling ``namedtuple``.
# We could also have done the following:
Pt = namedtuple('Point2D', ('x', 'y'))


# The ``namedtuple`` class name is `Point2D`, but the label we `Pt` simply points to that class, so we would then create instances of the `Point2D` class as follows:
pt1 = Pt(10, 20)


# And we can see what `pt1` is:
pt1


# As you can see we have an object of type `Point2D`, and it has two properties, `x` and `y` with respective values `10` and `20`.
# The only weird thing here is that we are using `Pt` to generate our instances of the `Point2D` class.
# That's why we usually always created `namedtuple` generated classes this way:
Point2D = namedtuple('Point2D', ('x', 'y'))


# Then the following makes more sense:
pt1 = Point2D(10, 20)
pt1


# This is not different than doing this:
Pt3 = Point3D  # class we defined earlier
pt3 = Pt3(10, 20, 30)
pt3


# As you can see above, we used another label `Pt3` as a label that also references the `Point3D` class. It would be weird to do it this way here, and its weird for tuples as well. Of course, you may run into circumstances where you need to do this - just not as a general rule.

# Note that all named tuples  are honest to goodness **classes**, just as if you had used a `class` definition such as with `Point3D`.
# The `namedtuple` function **generates** classes for us - it is a **class factory**.
type(Point3D)
type(Point2D)


# However, `Point2D` is a subclass of `tuple`, while `Point3D` is not:
isinstance(pt1, tuple)
isinstance(pt3, tuple)


# So, when we create an instance of a class, we are in fact calling the `__new__` method with our initial values. It's just a callable that has the **field names** we used to generate our named tuple class as its parameters. This means we can use keyword arguments when instantiating our named tuples!
pt4 = Point2D(y=20, x=10)
pt4


# #### What did we get for free using a named tuple vs our own class?

# First using a named tuple for our 2D point:
pt2d_1 = Point2D(10, 20)
pt2d_2 = Point2D(10, 20)
pt2d_1
pt2d_1 == pt2d_2


# Now using our 3D class:
pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)
pt3d_1


# Oh, we probably need to implement the `__repr__` method in our class
pt3d_1 == pt3d_2


# And we would also need to implement the __eq__ method!
# Let's do that:
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)
pt3d_1
pt3d_1 == pt3d_2


# How about finding the largest coordinate in the point?
# That's easy for `Point2D` since it is a tuple, but not the case for `Point3D`:
max(pt2d_1)
max(pt3d_1)


# How about calculating the dot product of two points (considering them as vectors starting at the origin)?

# The formula would be:
# a.b = a.x * b.x + a.y + b.y + a.z * b.z

# For the 3D point we would need to do the following:
def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z + b.z

dot_product_3d(pt3d_1, pt3d_2)


# But for our 2D point, which, remember is a tuple as well, we can write a generic function that would work equally well with a 3D named tuple too:
def dot_product(a, b):
    return sum(e[0] * e[1] for e in  zip(a, b))


# Here's a break down of how we implemented the dot product:

# First we zip up the components of `a` and `b` to get an iterable of tuples containing the x-coordinates in the 1st element, and the y-coordinates in the second tuple. Our zip will contain as many elements as there are dimensions.
a = Point2D(1, 2)
b = Point2D(10, 20)
print(a)
print(b)
print(tuple(a))
print(tuple(b))
print(list(zip(a, b)))


# Note that if we had more dimensions this would work equally well.
# Suppose we had 3 dimensions:
u = (1, 2, 3)
v = (10, 20, 30)
list(zip(u, v))


# Then we create a comprehension that multiplies the components together:
[e[0] * e[1] for e in zip(a, b)]


# Then we simply add those up:
sum([e[0] * e[1] for e in zip(a, b)])

dot_product(a, b)


# And if we defined a 4D point named tuple:
Point4D = namedtuple('Point4D', ['i', 'j', 'k', 'l'])

pt4d_1 = (1, 1, 1, 10)
pt4d_2 = (2, 2, 2, 10)

dot_product(pt4d_1, pt4d_2)


# As you can see we got the correct dot product. We could not have done this using our `Point3D` class!

# #### Other Ways to Specify Field Names

# There are a number of ways we can specify the field names for the named tuple:
# * we can provide a sequence of strings containing each property name
# * we can provide a single string with property names separated by whitespace or a comma
Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])
circle_1 = Circle(0, 0, 10)
circle_2 = Circle(center_x=10, center_y=20, radius=100)
circle_1
circle_2


# Or we can do it this way:
City = namedtuple('City', 'name country population')
new_york = City('New York', 'USA', 8_500_000)
new_york


# This would work equally well:
Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
djia


# In fact, since whitespace can be used we can even use a multi-line string!
Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
djia


# #### Accessing Items in a Named Tuple

# The major advantage of named tuples are that, as the name suggests, we can access the properties (fields) of the tuple by name:
pt1
pt1.x
circle_1
circle_1.radius


# Now named tuples *are* tuples, so elements can be accessed by index, unpacked, and iterated.
circle_1[2]
for item in djia:
    print(item)


# We can also unpack named tuples just like ordinary tuples:
pt1
x, y = pt1
print(x, y)


# We can also use extended unpacking:
djia
symbol, *_, close = djia
print(symbol, close)


# And remember that the `_` we use in the unpacking is just a regular variable:
print(_)


# The field names for these named tuples can be any valid variable name **except** that they cannot start with an underscore.
# For example the following would not be valid:
Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'])


# We can also choose to let the `namedtuple` function replace invalid field names automatically for us, by using the keyword argument `rename`. When we set that argument to `True` (it is `False` by default) it will replace the invalid name using the position (index) of the field, preceded by an underscore:
Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'], rename=True)
eric = Person('Eric', 'Idle', 42, 'unknown')
eric


# As you can see the invalid field name `_y` was replaced by `_1` since it was the second element (i.e. index of `1`)

# #### Named Tuple Internals

# We can easily find out the fields in a named tuple using the `_fields` property:
Point2D._fields
Stock._fields


# There is also a property, `_source` that allows us to see exactly the class that was generated by calling `namedtuple` (remember that `namedtuple` is a class **factory**):
print(Point2D._source)


# And of course this will be slightly different for another named tuple generated class:
print(Person._source)


# #### Converting Named Tuples to Dictionaries

# The `namedtuple` generated class also provides us an instance method, `_asdict()` that will create a dictionary from all the fields in the named tuple:
eric._asdict()


# Technically, it is an `OrderedDict` which we will cover in later section. Basically an `OrderedDict` is a dictionary that, unlike the standard built-in `Dictionary` is **guaranteed** to preserve the order of the keys.
# [**Note** that as of Python 3.6, regular dictionaries **do** preserve the order of the keys, but until just recently it was not **guaranteed** and was bascially an implementation detail.
# **However, this has now changed!!** Guido van Rossum has now agreed that this is no longer an implementation detail, and starting in Python 3.7 dictionary order is guaranteed. Since it is actually already the case in Python 3.6, you can now safely assume this fact - as long as you are running your code under Python 3.6 or higher. Your code will break if you rely on dictionary order prior to 3.6, in that case, still use an `OrderedDict`]

# #### Overhead of Named Tuples

# At this point you may be wondering whether there's more overhead to using a named tuple vs a regular tuple.
# There is, but it is tiny. The field names are stored in the **class**, not every instance of the named tuples.
# This means that the overhead incurred by the field names for one instance of the named tuple vs 1000 instances is the same. Otherwise, the instances are tuples, so you can access contained objects using indexing, slicing and iteration just as if it were a plain tuple. No overhead there either. Looking up values by name do have some overhead of course, but no more than if you had created a custom class.
