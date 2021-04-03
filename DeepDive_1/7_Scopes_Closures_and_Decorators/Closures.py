# %%
"""
### Closures
"""

# %%
"""
Let's examine that concept of a cell to create an indirect reference for variables that are in multiple scopes.
"""

# %%
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

# %%
fn = outer()

# %%
fn.__code__.co_freevars

# %%
"""
As we can see, `x` is a free variable in the closure.
"""

# %%
fn.__closure__

# %%
"""
Here we see that the free variable x is actually a reference to a cell object that is itself a reference to a string object.
"""

# %%
"""
Let's see what the memory address of `x` is in the outer function and the inner function. To be sure string interning does not play a role, I am going to use an object that we know Python will not automatically intern, like a list.
"""

# %%
def outer():
    x = [1, 2, 3]
    print('outer:', hex(id(x)))
    def inner():
        print('inner:', hex(id(x)))
        print(x)
    return inner

# %%
fn = outer()

# %%
fn.__closure__

# %%
fn()

# %%
"""
As you can see, each the memory address of `x` in `outer`, `inner` and the cell all point to the same object.
"""

# %%
"""
#### Modifying the Free Variable
"""

# %%
"""
We know we can modify nonlocal variables by using the `nonlocal` keyword. So the following will work:
"""

# %%
def counter():
    count = 0 # local variable
    
    def inc():
        nonlocal count  # this is the count variable in counter
        count += 1
        return count
    return inc

# %%
c = counter()

# %%
c()

# %%
c()

# %%
"""
##### Shared Extended Scopes
"""

# %%
"""
As we saw in the lecture, we can set up nonlocal variables in different inner functionsd that reference the same outer scope variable, i.e. we have a free variable that is shared between two closures. This works because both non local variables and the outer local variable all point back to the same cell object.
"""

# %%
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2

# %%
fn1, fn2 = outer()

# %%
fn1.__closure__, fn2.__closure__

# %%
"""
As you can see here, the `count` label points to the same cell.
"""

# %%
fn1()

# %%
fn1()

# %%
fn2()

# %%
"""
### Multiple Instances of Closures
"""

# %%
"""
Recall that **every** time a function is called, a **new** local scope is created.
"""

# %%
from time import perf_counter

def func():
    x = perf_counter()
    print(x, id(x))

# %%
func()

# %%
func()

# %%
"""
The same thing happens with closures, they have their own extended scope every time the closure is created:
"""

# %%
def pow(n):
    # n is local to pow
    def inner(x):
        # x is local to inner
        return x ** n
    return inner

# %%
"""
In this example, `n`, in the function `inner` is a free variable, so we have a closure that contains `inner` and the free variable `n`
"""

# %%
square = pow(2)

# %%
square(5)

# %%
cube = pow(3)

# %%
cube(5)

# %%
"""
We can see that the cell used for the free variable in both cases is **different**:
"""

# %%
square.__closure__

# %%
cube.__closure__

# %%
"""
In fact, these functions (`square` and `cube`) are **not** the same functions, even though they were "created" from the same `power` function:
"""

# %%
id(square), id(cube)

# %%
"""
### Beware!
"""

# %%
"""
Remember when I said the captured variable is a reference established when the closure is created, but the value is looked up only once the function is called?
"""

# %%
"""
This can create very subtle bugs in your program.
"""

# %%
"""
Consider the following example where we want to create some functions that can add 1, 2, 3, 4 and to whatever is passed to them.
"""

# %%
"""
We could do the following:
"""

# %%
def adder(n):
    def inner(x):
        return x + n
    return inner

# %%
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
add_4 = adder(4)

# %%
add_1(10), add_2(10), add_3(10), add_4(10)

# %%
"""
But suppose we want to get a little fancier and do it as follows:
"""

# %%
def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x: x + n)
    return adders

# %%
adders = create_adders()

# %%
"""
Now technically we have 4 functions in the `adders` list:
"""

# %%
adders

# %%
"""
The first one should add 1 to the value we pass it, the second should add 2, and so on.
"""

# %%
adders[3](10)

# %%
"""
Yep, that works for the 4th function.
"""

# %%
adders[0](10)

# %%
"""
Uh Oh - what happened? In fact we get the same behavior from every one of those functions:
"""

# %%
adders[0](10), adders[1](10), adders[2](10), adders[3](10)

# %%
"""
Remember what I said about when the variable is captured and when the value is looked up?
"""

# %%
"""
When the lambdas are **created** their `n` is the `n` used in the loop - the **same** `n`!!
"""

# %%
adders[0].__code__.co_freevars

# %%
adders[0].__closure__

# %%
adders[1].__closure__

# %%
adders[2].__closure__

# %%
adders[3].__closure__

# %%
"""
So, by the time we call `adder[i]`, the free variable `n` (shared between all adders) is set to 4.
"""

# %%
hex(id(4))

# %%
"""
As we can see the memory address of the singleton integer 4, is what that cell is pointint to.
"""

# %%
"""
If you want to use a loop to do this and not end up using the same cell for each of the free variables, we can use a simple trick that forces the evaluation of `n` at the time the closure is **created**, instead of when the closure function is evaluated.

We can do this by creating a parameter for `n` in our lambda whose default value is the current value of `n` - remember from an earlier video that parameter defaults are avaluated when the function is created, not called.
"""

# %%
def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders

# %%
adders = create_adders()

# %%
adders[0].__closure__

# %%
"""
Why aren't we getting anything in the closure? What about free variables?
"""

# %%
adders[0].__code__.co_freevars

# %%
"""
Hmm, nothing either... Why?

Well, look at the lambda in that loop. Does it reference the variable `n` (other than in the default value)? No. Hence, `n` is **not** a free variable in this case, and our lambda is just a plain lambda, not a closure.
"""

# %%
"""
And this code will now work as expected:
"""

# %%
adders[0](10)

# %%
adders[1](10)

# %%
adders[2](10)

# %%
adders[3](10)

# %%
"""
You just need to understand that since the default values are evaluated when the function (lambda in this case) is **created**, the then-current `n` value is assigned to the local variable `step`. So `step` will not change every time the lambda is called, and since n is not referenced inside the function (and therefore evaluated when the lambda is called), `n` is not a free variable.
"""

# %%
"""
#### Nested Closures
"""

# %%
"""
We can also nest closures, as can be seen in this example:
"""

# %%
def incrementer(n):
    def inner(start):
        current = start
        def inc():
            a = 10  # local var
            nonlocal current
            current += n
            return current
        return inc
    return inner
        

# %%
fn = incrementer(2)

# %%
fn

# %%
fn.__code__.co_freevars

# %%
fn.__closure__

# %%
inc_2 = fn(100)

# %%
inc_2

# %%
inc_2.__code__.co_freevars

# %%
inc_2.__closure__

# %%
"""
Here you can see that the second free variable `n`, is pointing to the same cell as the free variable in `fn`.
"""

# %%
"""
Note that **a** is a local variable, and is not considered a free variable.
"""

# %%
"""
And we can call the closures as follows:
"""

# %%
inc_2()

# %%
inc_2()

# %%
inc_3 = incrementer(3)(200)

# %%
inc_3()

# %%
inc_3()