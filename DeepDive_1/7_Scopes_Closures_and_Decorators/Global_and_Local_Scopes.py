# %%
"""
### Global and Local Scopes
"""

# %%
"""
In Python the **global** scope refers to the **module** scope.

The scope of a variable is normally defined by **where** it is (lexically) defined in the code.
"""

# %%
a = 10

# %%
"""
In this case, **a** is defined inside the main module, so it is a global variable.
"""

# %%
def my_func(n):
    c = n ** 2
    return c

# %%
"""
In this case, **c** was defined inside the function **my_func**, so it is **local** to the function **my_func**. In this example, **n** is also **local** to **my_func**
"""

# %%
"""
Global variables can be accessed from any inner scope in the module, for example:
"""

# %%
def my_func(n):
    print('global:', a)
    c = a ** n
    return c

# %%
my_func(2)

# %%
"""
As you can see, **my_func** was able to reference the global variable **a**.
"""

# %%
"""
But remember that the scope of a variable is determined by where it is assigned. In particular, any variable defined (i.e. assigned a value) inside a function is local to that function, even if the variable name happens to be global too!
"""

# %%
def my_func(n):
    a = 2
    c = a ** 2
    return c

# %%
print(a)
print(my_func(3))
print(a)

# %%
"""
In order to change the value of a global variable within an inner scope, we can use the **global** keyword as follows:
"""

# %%
def my_func(n):
    global a
    a = 2
    c = a ** 2
    return c

# %%
print(a)
print(my_func(3))
print(a)

# %%
"""
As you can see, the value of the global variable **a** was changed from within **my_func**.
"""

# %%
"""
In fact, we can **create** global variables from within an inner function - Python will simply create the variable and place it in the **global** scope instead of the **local scope**:
"""

# %%
def my_func(n):
    global var
    var = 'hello world'
    return n ** 2

# %%
"""
Now, **var** does not exist yet, since the function has not run:
"""

# %%
print(var)

# %%
"""
Once we call the function though, it will create that global **var**:
"""

# %%
my_func(2)

# %%
print(var)

# %%
"""
#### Beware!!
"""

# %%
"""
Remember that whenever you assign a value to a variable without having specified the variable as **global**, it is **local** in the current scope. **Moreover**, it does not matter **where** the assignment in the code takes place, the variable is considered local in the **entire** scope - Python determines the scope of objects at compile-time, not at run-time.
"""

# %%
"""
Let's see an example of this:
"""

# %%
a = 10
b = 100

# %%
def my_func():
    print(a)
    print(b)
    

# %%
my_func()

# %%
"""
So, this works as expected - **a** and **b** are taken from the global scope since they are referenced **before** being assigned a value in the local scope.

But now consider the following example:
"""

# %%
a = 10
b = 100

def my_func():
    print(a)
    print(b)
    b = 1000

# %%
my_func()

# %%
"""
As you can see, **b** in the line ``print(b)`` is considered a **local** variable - that's because the **next** line **assigns** a value to **b** - hence **b** is scoped as local by Python for the **entire** function.
"""

# %%
"""
Of course, functions are also objects, and scoping applies equally to function objects too. For example, we can "mask" the built-in `print` Python function:
"""

# %%
print = lambda x: 'hello {0}!'.format(x)

def my_func(name):
	return print(name)

my_func('world')


# %%
"""
You may be wondering how we get our **real** ``print`` function back!
"""

# %%
del print

# %%
print('hello')

# %%
"""
Yay!!
"""

# %%
"""
If you have experience in some other programming languages you may be wondering if loops and other code "blocks" have their own local scope too. For example in Java, the following would not work:
"""

# %%
"""
``for (int i=0; i<10; i++) {
    int x = 2 * i;
}
system.out.println(x);
``
"""

# %%
"""
But in Python it works perfectly fine:
"""

# %%
for i in range(10):
    x = 2 * i
print(x)

# %%
"""
In this case, when we assigned a value to `x`, Python put it in the global (module) scope, so we can reference it after the `for` loop has finished running.
"""