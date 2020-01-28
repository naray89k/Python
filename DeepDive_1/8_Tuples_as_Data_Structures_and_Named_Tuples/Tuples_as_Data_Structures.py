#!/usr/bin/env python
# coding: utf-8

# ### Tuples as Data Structures

# Tuples are an immutable container type.
# They contain a collection of objects. The tuple is a sequence type - this means order matters (and is preserved) and elements can be accessed by index (zero based), slicing, or iteration.
# Other common sequence types in Python include lists and strings. Strings, like tuples are immutable, whereas lists are mutable.
# Tuples are sometimes presented as immutable lists, but in fact, they could be compared more closely to strings with one major difference: strings are homogeneous sequences, while tuples can be heterogeneous.

# A tuple literal is often presented as:
('a', 10, True)


# But the parentheses are not what indicate a tuple - it is the commas:
a = ('a', 10, True)
b = 'b', 20, False
type(a)
type(b)


# Sometimes however, the parentheses are *required* to remove any ambiguity.
# For example, consider this function that expects a tuple (or other iterable) as its argument:
def iterate(t):
    for element in t:
        print(element)


# If we call the function this way, Python will interpret it as three arguments:
iterate(1, 2, 3)


# Instead, we now **have** to use the parentheses to indicate we are packing a tuple:
iterate((1, 2, 3))


# Since tuples are sequence types, we can access items by index:
a = 'a', 10, True
a[2]


# Or we can even slice them:
a = 1, 2, 3, 4, 5
a[2:4]


# We can iterate over them:
a = 1, 2, 3, 4, 5
for element in a:
    print(element)


# We can also use unpacking:
point = 10, 20, 30
x, y, z = point
print(x)
print(y)
print(z)


# Tuples are immutable, in the sense that we cannot change the reference of an object in the container and we cannot add or remove objects from the container. This is the same as strings.
a = 10, 'python', True
a[0] = 20


# We can however 'extend' tuples, but just as with strings, we are actually just creating a new tuple:
a = 1, 2, 3
id(a)
a = a + (4, 5, 6)
a
id(a)


# As you can see we no longer have the same memory address for `a`.

# We have to be careful when we think about immutability of tuples. The tuple, as a container is immutable, but the elements contained in the tuple may very well be mutable.

# Let's define a simple point class to store the x and y coordinates of a point in 2D space:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

a = Point2D(0, 0), Point2D(10, 10), Point2D(20, 20)
a


# Although the tuple `a` is immutable, its contained elements are mutable:

# So we cannot do this:
a[0] = Point2D(-10, -10)


# But we can modify the contents of the first element:
a[0].x = -10
a


# #### Tuples as Data Records

# We can interpret tuples as lightweight data structures where, by convention, the position of the element in the tuple has meaning.
# For example, we may elect to represent a point as a tuple, and not use the class approach we just did:
pt1 = (0, 0)
pt2 = (10, 10)


# Here, we simply decide that the first position of the tuple represents the x=coordinate while the second element represents the y-coordinate of a point in 2D space.

# We could also decide that we are going to represent a city using a tuple, where the first position will the city name, the second position will be the country, and the the third position will be the population:
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000


# We can even have a list of these tuples:
cities = london, new_york, beijing


# We can obtain a list of all the cities in the list using a simple list comprehension and the fact that the city name is the first element (index 0) of each tuple:
city_names = [t[0] for t in cities]
print(city_names)


# We could even calculate the total population of all these cities.
# We start with a simple loop to do this:
total = 0
for city in cities:
    total += city[2]
print (f'total={total}')


# You will note that the reason this worked is because the `cities` list contained **only** city tuples. The list was homogeneous. The tuples on the other hand are heterogeneous.
# This is often a key difference between lists and tuples, especially when we consider tuples as data structures. The tuples are heterogeneous, while the list needs to be homogeneous so we can apoply the same calculations to each element of the list.
# The above example would break if one of the elements in the `cities` list was an integer for example.

# Back to our example calculating the total population. There is a more Pythonic way of doing this.
# First we use a comprehension to extract just the population from each city :
[city[2] for city in cities]


# Next we simply sum up the population values:
sum([city[2] for city in cities])


# In fact (and we'll cover this in detail later in this course), we don't even need the square brackets in the sum:
sum(city[2] for city in cities)


# Now, since tuples are sequence types, and hence iterable, we can also use unpacking to extract values from the tuple:
city, country, population = new_york
print(city)
print(country)
print(population)


# We can also use extended unpacking:
record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072


# Where the structure is: symbol, year, month, day, open, high low, close

# We could then unpack the record using straight unpacking:
symbol, year, month, day, open_, high, low, close = record
print(symbol)
print(close)


# But suppose we are only interested in the symbol, year, month, day and close. Then we could use extended unpacking as follows:
symbol, year, month, day, *others, close = record
print(symbol, year, month, day, close)
print(others)


# A convetion often used in Python when we are not particularly interested in something, is to use an underscore as a variable name:
symbol, year, month, day, *_, close = record


# There's nothing special about the underscore here, it's just a legal variable name (in an interactive Python session, the underscore is actually used to store the results of the last calculation)
print(_)


# By the way do not write code like this to do the unpacking we just did:
symbol, year, close = record[0], record[1], record[7]


# Although this works, it is not very readable code, plus you are packing a new tuple (the right hand side) and then unpacking it into the variables on the left. Much better to do this:
symbol, year, *_, close = record


# If you only need to pick a few elements out of the tuple (like in our example where we just wanted the population to sum it up), then by all means access it directly using the index.

# But did you know that you can also unpack tuples directly in the loop?
for element in cities:
    print(element)


# As you can see, each element is a tuple, and we can actually unpack it at the same time as the loop this way:
for city, country, population in cities:
    print(f'city={city}, population={population}')


# This, by the way, is how we can use the `enumerate` function in Python. The enumerate function produces an iterable from another iterable but contains the index number. Values are returned as tuples, where the first position is the index value, and the second position is the value (here we also see how a tuple was used as a data structure). So that tuple can be unpacked as follows:
for index, value in enumerate(beijing):
    print(f'{index}: {value}')


# Of course, since we are not interested in the country in this case, we might write it this way as well:
for city, _, population in cities:
    print(f'city={city}, population={population}')


# Another frequent application of usign tuples as data structures is for returning multiple values from a function.
from random import uniform
from math import sqrt

def random_shot(radius):
    '''Generates a random 2D coordinate within
    the bounds [-radius, radius] * [-radius, radius]
    (a square of area 4)
    and also determines if it falls within
    a circle centered at the origin
    with specified radius'''

    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle

num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')
