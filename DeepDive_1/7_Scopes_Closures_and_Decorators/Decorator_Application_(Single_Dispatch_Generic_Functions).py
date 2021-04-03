# %%
"""
### Decorator Application: Single Dispatch Generic Functions
"""

# %%
"""
Consider an application where we want to provide similar functionality but that varies slightly depending on the argument types passed in.

In this set of examples we consider this problem where functionality differs based on a single argument's type (hence single dispatch) instead of the type of multiple arguments (which would be multi dispatch)
"""

# %%
"""
If you have a background in some other OO languages such as Java or C#, you'll know that we can easily do something like this by basically **overloading** functions: using a different data type for the function parameter, hence changing the function signature. Then although the name of the function is the same, calling `do_something(100)` and `do_something('java')` would call a different function, the first one would call the `do_something(int)` function, and the second would call the `do_something(String)` function.

Of course, Python is not statically typed, so even if Python had function overloading built-in, we would not be able to make such a distinction in our function signatures since there is nothing that says that a parameter must be of a specific type, so in a best case scenario we would have to "distinguish" functions with the same name only by the number of parameters they take. And then we'd have to somehow deal with variable numbers of positional and keyword arguments too... Uuugh!
In any event, single dispatch could never work.

Instead we have to come up with a different solution.
"""

# %%
"""
Let's say we want to display various data types in html format, with different presentations for integers (we want both base 10 and hex values), floats (we always want it rounded to 2 decimal points), strings (we want the string html-escaped, and all newline characters replaced by `<br/>`), lists and tuples should be implemented using bulleted lists, and the same with dictionaries except we want the name/value pair to be displayed in the bulleted list.
"""

# %%
"""
For starters, let's just implement individual functions to do each of those things.

I am going to keep the functions very simple, but in practice you should handle situations like None objects, empty lists and dictionaries, possibly the wrong type being passed to the function, etc.
"""

# %%
from html import escape

def html_escape(arg):
    return escape(str(arg))
                      
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))
                                  
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')
                                  
def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item)) 
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
                                  
def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), html_escape(v)) 
             for k, v in d.items())    
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# %%
print(html_str("""this is 
a multi line string
with special characters: 10 < 100"""))

# %%
print(html_int(255))

# %%
print(html_escape(3+10j))

# %%
"""
Ideally we would want to just have to call a single function, maybe `htmlize` that would figure out which particular flavor of the `html_xxx` function to call depending on the argument type.
"""

# %%
"""
We could try it as follows:
"""

# %%
from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))

# %%
"""
Now we can essentially use the same function call to handle different types - the `htmlize` function is a dispatcher - it dispatches the request to a different function based on the argument type. (There's a much better way to do some of this, but we'll have to wait until we cover abstract base classes to do so).
"""

# %%
print(htmlize([1, 2, 3]))

# %%
print(htmlize(dict(key1=1, key2=2)))

# %%
print(htmlize(255))

# %%
"""
But there are a number of shortcomings here:
"""

# %%
print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))

# %%
"""
As you can see, the multi-line string did not get the newline characters replaced, the tuple was not rendered as an html list, and the integers do not have their hex representation.

So we just need to redefine the `html_list` and `html_dict` functions to use the `htmlize` function:
"""

# %%
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# %%
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# %%
print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))

# %%
"""
Much better, but hopefully you spotted something that might seem problematic!

Do we not have a circular reference?

In order to define `html_list` and `html_dict` we needed to call `htmlize`, but in order to define `htmlize` we needed to call `html_list` and `html_dict`.
"""

# %%
"""
Remember that in Python we can reference a function **inside** the body of another function **before** the function has been defined, as long as by the time we **call** the first function, the second one has been defined. SO this is actually OK.

If you don't believe me and want to make sure of this yourself, go ahead and reset your Kernel (click on the Kernel | Restart menu option), and run the following code without running anything prior to this.

The `htmlize` function body makes calls to other functions such as `html_escape`, `html_int`, etc that have not actually been defined yet
"""

# %%
from html import escape
from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))

# %%
"""
Now we define all the functions that `htmlize` uses before we actually call `htmlize` and all is good:
"""

# %%
def html_escape(arg):
    return escape(str(arg))
                      
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))
                                  
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')
                                  
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
                                  
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# %%
print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))

# %%
"""
As you can see this works just fine.

But we still have something undesirable. You'll notice that the dispatch function `htmlize` needs to have this big `if...elif...else` statement that will just keep growing as we need to handle more and more types (including potentially custom types).

This will just get unwieldy, and not very flexible (every time someone creates a new type that has to have a special html representation they will need to go into the `htmlize` function and modify it.
"""

# %%
"""
So instead, we are going to try a more flexible approach using decorators.
"""

# %%
"""
The way we are going to approach this is to create a dispatcher function, and then separately "register" each type-specific function with the dispatcher.
"""

# %%
"""
First, we are going to create a decorator that will do something that may seem kind of silly - it is going to take the decorated function and store it in a dictionary, using a key consisting of the **type** `object`.

Then when the returned closure is called, the closure will call the function stored in that dictionary.
"""

# %%
def singledispatch(fn):
    registry = dict()
    registry[object] = fn
    
    def inner(arg):
        return registry[object](arg)

    return inner

# %%
@singledispatch
def htmlizer(arg):
    return escape(str(arg))

# %%
htmlizer('a < 10')

# %%
"""
Next, we are going to add some functions to that `registry` dictionary, and modify our inner function to choose the correct function from the registry, or pick a default based on the type of the argument:
"""

# %%
def singledispatch(fn):
    registry = dict()
    
    registry[object] = fn
    registry[int] = lambda arg: '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))
    registry[float] = lambda arg: '{0:.2f}'.format(round(arg, 2))
    
    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    return inner

# %%
@singledispatch
def htmlize(a):
    return escape(str(a))

# %%
htmlize(10)

# %%
htmlize(3.1415)

# %%
"""
Now, we want a way to add the specialized functions to the `registry` dictionary from **outside** the `singledispatch` function - to do so we will create a parametrized decorator that will (1) take the type as a parameter, and (2) return a closure that will decorate the function associated with the type:
"""

# %%
def singledispatch(fn):
    registry = dict()
    
    registry[object] = fn
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
        return inner
        
    
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    
    return decorator

# %%
"""
But of course this is not good enough - how do we get a hold of the `register` function from outside `singledispatch`? Remember, `singledispatch` is a decorator that returns the `decorated` closure, not the `register` closure.
"""

# %%
"""
We can do this by adding the `register` function as an **attribute** of the `decorated` function before we return it. 

While we're at it we're also going to:

* add the `registry` dictionary as an attribute as so we can look into it to see what it contains.

* add another function that given a type will return the function associated with that type (or the default function if the type is not found in the dictionary)
"""

# %%
def singledispatch(fn):
    registry = dict()
    
    registry[object] = fn
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner
   
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    
    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator

# %%
@singledispatch
def htmlize(arg):
    return escape(str(arg))

# %%
"""
And we can see that `htmlize` (that returned `inner`) function has an attribute called `register`:
"""

# %%
htmlize.register

# %%
"""
as well as that `registry` attribute that we put in just we could see what keys are in the `registry` dictionary:
"""

# %%
htmlize.registry

# %%
"""
We can also ask it what function it is going to use for any specific type (currently we only have one registered, the default, for the most general `object` type):
"""

# %%
htmlize.dispatch(str)

# %%
"""
And you'll note that the extended scope of `register` and `dispatch` is the same as the extended scope of `htmlize`.
"""

# %%
"""
So now we can register some functions (it will store the function with associated data type in the `registry` dictionary):
"""

# %%
@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

# %%
"""
We can peek into the registered types:
"""

# %%
htmlize.registry

# %%
"""
and we can ask the decorated `htmlize` function what function it is going to use for the `int` type:
"""

# %%
htmlize.dispatch(int)

# %%
"""
and we can actually call it as well:
"""

# %%
htmlize(100)

# %%
"""
The huge advantage now is that we can keep registering new handlers from anywhere in our module, or even from outside our module!
"""

# %%
@htmlize.register(float)
def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict)
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(htmlize(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# %%
htmlize.registry

# %%
print(htmlize([1, 2, 3]))

# %%
print(htmlize((1, 2, 3)))

# %%
print(htmlize("""this
is a multi line string with
a < 10"""))

# %%
"""
Our single dispatch decorator works quite well - but it has some limitations. For example it cannot handle functions that take in more than one argument (in which case dispatching would be based on the type of the **first** argument), and we also are not allowing for types based on parent classes - for example, integers and booleans are both integral numbers - i.e. they both inherit from the Integral base class. Similarly lists and tuples are both more generic Sequence types. We'll see this in more detail when we get to the topic of abstract base classes (ABC's).
"""

# %%
from numbers import Integral

# %%
isinstance(100, Integral)

# %%
isinstance(True, Integral)

# %%
isinstance(100.5, Integral)

# %%
type(100) is Integral

# %%
type(True) is Integral

# %%
(100).__class__

# %%
(True).__class__

# %%
"""
The way we have implement our decorator, if we register an Integral generic function, it won't pick up either integers or Booleans.

We can certainly fix this shortcoming ourselves, but of course...

We can can use Python's built-in single dispatch support, in ...

you guessed it!

the `functools` module.
"""

# %%
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

# %%
@singledispatch
def htmlize(a):
    return escape(str(a))

# %%
"""
The `singledispatch` returned closure has a few attributes we can use:
1. A `register` decorator (just like ours did)
2. A `registry` property that is the registry dictionary
3. A `dispatch` function that can be used to determine which registry key (registered type) it will use for the specified type.
"""

# %%
@htmlize.register(Integral)
def htmlize_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a))) 

# %%
htmlize.dispatch(int)

# %%
htmlize.dispatch(bool)

# %%
htmlize(100)

# %%
htmlize(True)

# %%
@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# %%
htmlize.dispatch(list)

# %%
htmlize.dispatch(tuple)

# %%
htmlize.dispatch(str)

# %%
"""
You'll note that a string is also a sequence type, hence our dispatcher will call the `html_sequence` function on a string.
"""

# %%
"""
In fact, at this point things would not even run properly.

If we were to call

`htmlize('abc')`

we'd get an infinite recursion!

The call to `htmlize` the string `abc` would treat it as a sequence, which would call `htmlize` character by character. But each character is itself just a string of length 1, so it will `htmlize` for that single character, which would treat it as a sequence, which would call `htmlize` for that single character again, and so on, in an infinite loop. 
"""

# %%
htmlize('abc')

# %%
"""
Instead, we are going to register a string handler specifically - that way we will avoid that problem entirely:
"""

# %%
@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

# %%
htmlize.dispatch(str)

# %%
"""
So, even though a string is both an `str` instance and in general a sequence type, the "closest" type will be picked by the dispatcher (again something our own implementation did not do).

This means, we have something for generic sequences, but something specific for more specialized strings.
"""

# %%
htmlize('abc')

# %%
"""
We can do the same thing with sequences - right now `html_sequence` will be used for both lists and tuples. 
"""

# %%
"""
But suppose we want slightly different handling of tuples:
"""

# %%
@htmlize.register(tuple)
def html_tuple(t):
    items = [escape(str(item)) for item in t]
    return '({0})'.format(', '.join(items))

# %%
htmlize.dispatch(list)

# %%
htmlize.dispatch(tuple)

# %%
print(htmlize(['a', 100, 3.14]))

# %%
print(htmlize(('a', 100, 3.14)))

# %%
"""
One thing of note is that we started our decoration with a `@singledispatch` decorator - you'll notice that no specific type was indicated here - and in fact this means the dispatcher will use the generic `object` type.
"""

# %%
"""
This means that any object type not specifically handled by our dispatcher will fall back on that `object` key - hence you can think of it as the default for the dispatcher.
"""

# %%
type(None)

# %%
htmlize.dispatch(type(None))

# %%
type(1+1j)

# %%
htmlize.dispatch(complex)

# %%
type(3)

# %%
htmlize.dispatch(int)

# %%
"""
Lastly, because the name of the individual specialized functions does not really matter to us (the dispatcher will pick the appropriate function), it is quite common for an underscore character ( \_ ) to be used for the function name - the memory address of each specialized function will be stored in the `registry` dictionary, and the function name does not matter - in fact we can even add lambdas to the registry.
"""

# %%
@singledispatch
def htmlize(a):
    return escape(str(a))

# %%
@htmlize.register(int)
def _(a):
    return '{0}({1})'.format(a, str(hex(a)))

# %%
@htmlize.register(str)
def _(s):
    return escape(s).replace('\n', '<br/>\n')

# %%
htmlize.register(float)(lambda f: '{0:.2f}'.format(f))

# %%
htmlize.registry

# %%
"""
But note that the `__main__._` function for `int` and `str` are not the same functions (even tough they have the same name):
"""

# %%
id(htmlize.registry[str])

# %%
id(htmlize.registry[int])

# %%
"""
And everything works as expected:
"""

# %%
htmlize(100)

# %%
htmlize(3.1415)

# %%
print(htmlize("""this
is a multi-line string
a < 10"""))

# %%
"""
If this same name but different function thing has you confused, look at it this way:
"""

# %%
def my_func():
    print('my_func initial')

# %%
id(my_func)

# %%
f = my_func

# %%
id(f)

# %%
"""
So, `f` and `my_func` point to the same function in memory.

Let's go ahead and "redefine" the function `my_func`:
"""

# %%
def my_func():
    print('second my_func')

# %%
"""
In fact, we did not "redefine" the previous `my_func`, it still exists in memory (and `f` still points to it). Instead we have re-assigned the function that `my_func` points to:
"""

# %%
id(my_func)

# %%
"""
But the original `my_func` is still around, and 'f' still has a reference to it:
"""

# %%
id(f)

# %%
"""
So, we can call each one:
"""

# %%
f()

# %%
my_func()

# %%
"""
But the function `__name__` have the same value:
"""

# %%
f.__name__

# %%
my_func.__name__

# %%
"""
Just always keep in mind that labels point to something in memory, it is not the object itself. So in this case we have two distinct objects (functions) which happen to have the same name, but are two very different objects - `f` points to the first one we created, and `my_func` points to the second.
"""