# %%
"""
### Decorators (Part 1)
"""

# %%
"""
Recall the example in the last section where we wrote a simple closure to count how many times a function had been run:
"""

# %%
def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

# %%
def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b

# %%
help(add)

# %%
"""
Here's the memory address that `add` points to:
"""

# %%
id(add)

# %%
"""
Now we create a closure using the `add` function as an argument to the `counter` function:
"""

# %%
add = counter(add)

# %%
"""
And you'll note that `add` is no longer the same function as before. Indeed the memory address `add` points to is no longer the same:
"""

# %%
id(add)

# %%
add(1, 2)

# %%
add(2, 2)

# %%
"""
What happened is that we put our **add** function 'through' the **counter** function - we usually say that we **decorated** our function **add**.

And we call that **counter** function a **decorator**.

There is a shorthand way of decorating our function without having to type:

``func = counter(func)``
"""

# %%
@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c

# %%
mult(1, 2, 3)

# %%
mult(2, 2, 2)

# %%
"""
Let's do a little bit of introspection on our two decorated functions:
"""

# %%
add.__name__

# %%
mult.__name__

# %%
"""
As you can see, the name of the function is no longer **add** or **mult**, but instead it is the name of that **inner** function in our decorator.
"""

# %%
help(add)

# %%
help(mult)

# %%
"""
As you can see, we've also lost our docstring and parameter annotations!
"""

# %%
"""
What about introspecting the parameters of **add** and **mult**:
"""

# %%
import inspect

# %%
inspect.getsource(add)

# %%
inspect.getsource(mult)

# %%
"""
Even the signature is gone:
"""

# %%
inspect.signature(add)

# %%
inspect.signature(mult)

# %%
"""
Even the parameter defaults documentation is are gone:
"""

# %%
inspect.signature(add).parameters

# %%
"""
In general, when we create decorated functions, we end up "losing" a lot of the metadata of our original function!
"""

# %%
"""
However, we **can** put that information back in - it can get quite complicated.

Let's see how we might be able to do that for some simple things, like the docstring and the function name.
"""

# %%
def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

# %%
@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b

# %%
help(add)

# %%
add.__name__

# %%
"""
At least we have the docstring and function name back... But what about the parameters? Our real **add** function takes two positional parameters, but because the closure used a generic way of accepting **\*args** and **\*\*kwargs**, we lose this information
"""

# %%
"""
We can use a special function in the **functools** module, called **wraps**. In fact, that function is a decorator itself!
"""

# %%
from functools import wraps

# %%
def counter(fn):
    count = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner

# %%
@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b

# %%
help(add)

# %%
"""
Yay!!! Everything is back to normal.
"""

# %%
inspect.getsource(add)

# %%
inspect.signature(add)

# %%
inspect.signature(add).parameters