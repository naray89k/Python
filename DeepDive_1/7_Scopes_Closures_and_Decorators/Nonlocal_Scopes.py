# %%
"""
### Nonlocal Scopes
"""

# %%
"""
Functions defined inside anther function can reference variables from that enclosing scope, just like functions can reference variables from the global scope.
"""

# %%
def outer_func():
    x = 'hello'
    
    def inner_func():
        print(x)
    
    inner_func()

# %%
outer_func()

# %%
"""
In fact, any level of nesting is supported since Python just keeps looking in enclosing scopes until it finds what it needs (or fails to find it by the time it finishes looking in the built-in scope, in which case a runtime error occurrs.)
"""

# %%
def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

# %%
outer_func()

# %%
"""
But if we **assign** a value to a variable, it is considered part of the local scope, and potentially **masks** enclsogin scope variable names:
"""

# %%
def outer():
    x = 'hello'
    def inner():
        x = 'python'
    inner()
    print(x)

# %%
outer()

# %%
"""
As you can see, **x** in **outer** was not changed.
"""

# %%
"""
To achieve this, we can use the **nonlocal** keyword:
"""

# %%
def outer():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
    inner()
    print(x)

# %%
outer()

# %%
"""
Of course, this can work at any level as well:
"""

# %%
def outer():
    x = 'hello'
    
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)

# %%
outer()

# %%
"""
How far Python looks up the chain depends on the first occurrence of the variable name in an enclosing scope.

Consider the following example:
"""

# %%
def outer():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer:', x)

# %%
outer()

# %%
"""
What happened here, is that `x` in `inner1` **masked** `x` in `outer`. But `inner2` indicated to Python that `x` was nonlocal, so the first local variable up in the enclosing scope chain Python found was the one in `inner1`, hence `x` in `inner2` is actually referencing `x` that is local to `inner1`
"""

# %%
"""
We can change this behavior by making the variable `x` in `inner` nonlocal as well:
"""

# %%
def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer:', x)

# %%
outer()

# %%
x = 100
def outer():
    x = 'python'  # masks global x
    def inner1():
        nonlocal x  # refers to x in outer
        x = 'monty' # changed x in outer scope
        def inner2():
            global x  # refers to x in global scope
            x = 'hello'
            print('inner1 (before):', x)
            inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer', x)    

# %%
outer()
print(x)

# %%
"""
But this will not work. In `inner` Python is looking for a local variable called `x`. `outer` has a label called `x`, but it is a global variable, not a local one - hence Python does not find a local variable in the scope chain.
"""

# %%
x = 100
def outer():
    global x
    x = 'python'
    
    def inner():
        nonlocal x
        x = 'monty'
    inner()

# %%
