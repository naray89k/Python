# %%
"""
### Decorators Application (Logger, Stacked Decorators)
"""

# %%
"""
In this example we're going to create a utility decorator that will log function calls (to the console, but in practice you would be writing your logs to a file (e.g. using Python's built-in logger), or to a database, etc.
"""

# %%
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(fn.__name__, run_dt))
        return result
        
    return inner

# %%
@logged
def func_1():
    pass

# %%
@logged
def func_2():
    pass

# %%
func_1()

# %%
func_2()

# %%
"""
Now we may additionaly also want to time the function. We can certainly include the code to do so in our `logged` decorator, but we could also just use the `@timed` decorator we already wrote by **stacking** our decorators.
"""

# %%
def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    
    return inner

# %%
@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

# %%
factorial(10)

# %%
"""
Note that the order in which we stack the decorators can make a difference!
"""

# %%
"""
Remember that this is because our stacked decorators essentially amounted to:
"""

# %%
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

factorial = timed(logged(factorial))

# %%
"""
So in this case the `timed` decorator will be called first, followed by the `logged` decorator.

You may wonder why the printed output seems reversed. Look at how the decorators were defined - they first ran the function passed in, and **then** printed the result.

So in the above example, a simplified look at what happens in each decorator:

* `timed(fn)(*args, **kwargs)`:
    1. calls `fn(*args, **kwargs)`
    2. prints timing
    
    
* `logged(fn)(*args, **kwargs)`:
    1. calls `fn(*args, **kwargs)`
    2. prints log info

So, calling
`factorial = timed(logged(factorial))`

is equivalent to:

<pre>
fn = logged(factorial)
factorial = timed(fn)

factorial(n) --> call timed(fn)(n)
             --> call fn(n), then print timing
             --> call logged(original_factorial)(n), then print timing
             --> call original_factorial(n), then log, then print timing
</pre>

So as you can see, the `timed` decorator ran first, but it called the logged decorated function first, then printed the result - hence why the print output seems reversed.
"""

# %%
factorial(10)

# %%
"""
But in the following case, the `logged` decorator will run first, followed by the `timed` decorator:
"""

# %%
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

factorial = logged(timed(factorial))

# %%
factorial(10)

# %%
"""
Or, using the **@** notation:
"""

# %%
@logged
@timed
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

# %%
factorial(10)

# %%
@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

# %%
factorial(10)

# %%
"""
To make this clearer, let's write two very simple decorators as follows:
"""

# %%
def dec_1(fn):
    def inner():
        print('running dec_1')
        return fn()
    return inner

# %%
def dec_2(fn):
    def inner():
        print('running dec_2')
        return fn()
    return inner

# %%
@dec_1
@dec_2
def my_func():
    print('running my_func')

# %%
my_func()

# %%
"""
But if we change the order of the decorators:
"""

# %%
@dec_2
@dec_1
def my_func():
    print('running my_func')

# %%
my_func()

# %%
"""
You may wonder whether this really matters in practice. And yes, it can.

Consider an API that contains various functions that can be called. However, endpoints are secured and can only be run by authenticated users who have some specific role(s). If they do not have the role you want to return an unauthorized error. But if they do, then you want to log that they called the endpoint.

In this case you may have one decorator that is used to check authentication and permissions (and immediately return an unauthorized error from the API if applicable), and the other to log the call. 

If you decorated it this way:

<pre>
@log
@authorize
def my_endpoint():
    pass
</pre>

then the call would always be logged.

But, in this instance:

<pre>
@authorize
@log
def my_endpoint():
    pass
</pre>

your endpoint would only get logged if the user passed the `authorize` test.
"""