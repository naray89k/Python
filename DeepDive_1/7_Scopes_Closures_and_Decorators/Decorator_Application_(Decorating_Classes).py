# %%
"""
### Decorator Application: Decorating Classes
"""

# %%
"""
We have so far worked with decorating functions. This means we can decorate functions defined with a `def` statement (we can use the `@` syntax, or the long form). Since class methods are functions, they can be decorated too. Lambda expressions can also be decorated (using the long form).
"""

# %%
"""
But if you think about how our decorators work, they take a single parameter, a function, and return some other function - usually a closure that uses the original function that was passed as an argument.
"""

# %%
"""
We could use the same concept to accept, not a function, but a class instead. We could reference that class inside our decorator, modify it, and then return that modified class.
"""

# %%
"""
First we look at something called **monkey patching**. It boils down to modifying or extending our code at **run time**.

For example we can modify or add attributes to classes at run time. Modules too.

In Python, many of the classes we use can be modified at run time 
(built-ins like strings, lists, and so on, cannot).

But classes written in Python, such as the ones we write, and even library classes, as long as they are written in Python, not C, can. For example `Fraction` in the `fractions` module can be monkey patched.

Just because we can do something however, does not mean we should! Monkey patching can be extremely useful, but don't do it just because you can - as always there should be a real reason to do it, as we'll see in a bit.

Also, in general it is a bad idea to monkey patch the special methods `__???__` (such as `__len__`) as this will often not work due to how these methods are searched for by Python.
"""

# %%
from fractions import Fraction

# %%
Fraction.speak = lambda self: 'This is a late parrot.'

# %%
f = Fraction(2, 3)

# %%
f

# %%
f.speak()

# %%
"""
Yes, this is obviously nonsense, but you get the idea that you can add attributes to classes even if you do not have direct control over the class, or after your class has been defined.
"""

# %%
"""
If you want a more useful method, how about one that tells us if the Fraction is an integral number? (i.e. denominator is `1`)
"""

# %%
Fraction.is_integral = lambda self: self.denominator == 1

# %%
f1 = Fraction(1, 2)
f2 = Fraction(10, 5)

# %%
f1.is_integral()

# %%
f2.is_integral()

# %%
"""
Now, we can make this change to the class by calling a function to do it instead:
"""

# %%
def dec_speak(cls):
    cls.speak = lambda self: 'This is a very late parrot.'
    return cls

# %%
Fraction = dec_speak(Fraction)

# %%
"""
_(Hopefully the above code reminds you of decorators.)_
"""

# %%
f = Fraction(10, 2)

# %%
f.speak()

# %%
"""
We can use that function to decorate our custom classes too, using the short **@** syntax too.
"""

# %%
@dec_speak
class Parrot:
    def __init__(self):
        self.state = 'late'

# %%
polly = Parrot()

# %%
polly.speak()

# %%
"""
Using this technique we could for example add a useful *reciprocal* attribute to the Fraction class, but of course since it would probably be a one time kind of thing (how many Fraction classes are there that you will want to add a reciprocal to after all), there's no need for decorators. Decorators  are useful when they are able to be reused in more general ways.
"""

# %%
Fraction.recip = lambda self: Fraction(self.denominator, self.numerator)

# %%
f = Fraction(2,3)

# %%
f

# %%
f.recip()

# %%
"""
These example are quite trivial, and not very useful. 

So why bring this up? 

Because this same technique can be used for more interesting things.
"""

# %%
"""
As a first example, let's say you typically like to inspect various properties of an object for debugging purposes, maybe the memory address, it's current state (property values), and the time at which the debug info was generated.
"""

# %%
from datetime import datetime, timezone

# %%
def debug_info(cls):
    def info(self):
        results = []
        results.append('time: {0}'.format(datetime.now(timezone.utc)))
        results.append('class: {0}'.format(self.__class__.__name__))
        results.append('id: {0}'.format(hex(id(self))))
        
        if vars(self):
            for k, v in vars(self).items():
                results.append('{0}: {1}'.format(k, v))
        
        # we have not covered lists, the extend method and generators,
        # but note that a more Pythonic way to do this would be:
        #if vars(self):
        #    results.extend('{0}: {1}'.format(k, v) 
        #                   for k, v in vars(self).items())
        
        return results
    
    cls.debug = info
    
    return cls

# %%
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        
    def say_hi():
        return 'Hello there!'

# %%
p1 = Person('John', 1939)

# %%
p1.debug()

# %%
"""
And of course we can decorate other classes this way too, not just a single class:
"""

# %%
@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed_mph):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed_mph = top_speed_mph
        self.current_speed = 0
    
    @property
    def speed(self):
        return self.current_speed
    
    @speed.setter
    def speed(self, new_speed):
        self.current_speed = new_speed

# %%
s = Automobile('Ford', 'Model T', 1908, 45)

# %%
s.debug()

# %%
s.speed = 20

# %%
s.debug()

# %%
from math import sqrt

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return 'Point({0},{1})'.format(self.x, self.y)

# %%
p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0,0)

# %%
abs(p1)

# %%
p1, p2

# %%
p1 == p2

# %%
"""
Hmm, we probably would have expected `p1` to be equal to `p2` since it has the same coordinates. But by default Python will compare memory addresses, since our class does not implement the `__eq__` method used for `==` comparisons.
"""

# %%
p2, p3

# %%
p2 > p3

# %%
"""
So, that class does not support the comparison operators such as `<`, `<=`, etc. 

Even `==` does not work as expected - it will use the memory address instead of using a comparison of the `x` and `y` coordinates as we might probably expect.
"""

# %%
"""
For the `<` operator, we need our class to implement the `__lt__` method, and for `==` we need the `__eq__` method.

Other comparison operators are supported by implementing a variety of functions such as `__le__` (`<=`), `__gt__` (`>`), `__ge__` (`>=`).

We are going to add the `__lt__` and `__eq__` methods to our Point class.

We will consider a Point object to be smaller than another one if it is closer to the origin (i.e. smaller magnitude).
"""

# %%
del Point

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented
            
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented
        
    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, self.x, self.y)

# %%
p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0,0)

# %%
p1, p2, p1==p2

# %%
p2, p3, p2==p3

# %%
"""
As we can see, `==` now works as expected
"""

# %%
p4 = Point(1, 2)

# %%
abs(p1), abs(p4), p1 < p4

# %%
"""
Great, so now we have `<` and `==` implemented. What about the rest of the operators: `<=`, `>`, `>=`?
"""

# %%
p1 > p4

# %%
"""
Ooh, since we have implemented `<` and `==`, does this mean Python magically implemented a `>` operator (i.e. not < and not ==)?
"""

# %%
"""
Not exactly! What happened is that since `p1` and `p4` are both points, running the comparison `p1 > p4` is really the same as evaluating `p4 < p1` - and Python did do that automatically for us.

But it has not implemented any of the others, such as `>=` and `<=`:
"""

# %%
p1 <= p4

# %%
"""
Now, although we could proceed in a similar way and define `>=`, `<=` and `>` using the same technique, observe that if `<` and `==` is defined then:

* `a <= b` iff `a < b or a == b`
* `a > b` iff `not(a<b) and a != b`
* `a >= b` iff `not(a<b)`
"""

# %%
"""
So, to be quite generic we could create a decorator that will implement these last three operators as long as `==` and `<` are defined. We could then decorate **any** class that implements just those two operators.
"""

# %%
def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls

# %%
"""
In reality, the code above is **NOT** a good implementation at all. We are not checking that the types are compatible and returning a `NotImplemented` result if appropriate. I am also using inline operators (`<` and `==`) instead of the dunder functions (`__lt__` and `__eq__`). I just kept it simple because we'll use a better alternative in a bit.
"""

# %%
"""
For example, a better way to implement `__ge__` would be as follows:
"""

# %%
def ge_from_lt(self, other):
    # self >= other iff not(other < self)
    result = self.__lt__(other)
    if result is NotImplemented:
        return NotImplemented
    else:
        return not result

# %%
"""
You may be wondering why I used `__lt__` instead of just using the `<` operator. This is because I want to actually look at the result of the operation without raising an exception if the operation is not implemented. The way I have the total ordering decorator implemented could cause an infinite loop because when I evaluate `self < other`, if an exception is raised, Python will reflect the evaluation to `other > self`, and if that raises an error as well, Python will try to reflect that operation too, and we get into an infinite loop (which eventually terminates in a stack overflow). This was actually a bug in Python's standard library implementation of a `complete_ordering` decorator (called `total_ordering`) that was resolved in 3.4.
"""

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented
            
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented
        
    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__, self.x, self.y)

# %%
Point = complete_ordering(Point)        

# %%
p1, p2, p3 = Point(1, 1), Point(3, 4), Point(3, 4)

# %%
abs(p1), abs(p2), abs(p3)

# %%
p1 < p2, p1 <= p2, p1 > p2, p1 >= p2, p2 > p2, p2 >= p3

# %%
"""
Now the `complete_ordering` decorator can also be directly applied to any class that defines `__eq__` and `__lt__`.
"""

# %%
@complete_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)
     
    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)
    
    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented
        

# %%
g1 = Grade(10, 100)
g2 = Grade(20, 30)
g3 = Grade(5, 50)

# %%
g1 <= g2, g1 == g3, g2 > g3

# %%
"""
Often, given the `==` operator and just **one** of the other comparison operators (`<`, `<=`, `>`, `>=`), then all the rest can be derived.

Our decorator insisted on `==` and `<`. but we could make it better by insisting on `==` and any one of the other operators. This will of course make our decorator more complicated, and in fact, Python has this precise functionality built in to the, you guessed it, `functools` module!

It is a decorator called `total_ordering`. 

Let's see it in action:
"""

# %%
from functools import total_ordering

# %%
@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)
     
    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)
    
    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented

# %%
g1, g2 = Grade(80, 100), Grade(60, 100)

# %%
g1 >= g2, g1 > g2

# %%
"""
Or we could also do it this way:
"""

# %%
@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)
     
    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)
    
    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent > other.score_percent
        else:
            return NotImplemented

# %%
g1, g2 = Grade(80, 100), Grade(60, 100)

# %%
g1 >= g2, g1 > g2, g1 <= g2, g1 < g2