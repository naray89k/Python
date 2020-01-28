#!/usr/bin/env python
# coding: utf-8

# #### Import Variants and Misconceptions

# I would like to briefly discuss the various import variants such as:
# * `import math`
# * `from math import sqrt, abs`
# * `from math import *`
# * `import math as r_math`
# * `from math import sqrt as r_sqrt`

# ##### import math

# * loads the entire module (`math`) in memory if it's not already there
# * adds a reference to it in `sys.modules` with a key of `math`
# * adds a symbol of the same name (`math`) in our current namespace referencing the `math` object

# ##### import math as r_math

# * loads the entire module (`math`) in memory if it's not already there
# * adds a reference to it in `sys.modules` with a key of `math`
# * adds the symbol `r_math` to our current namespace referencing the `math` object

# ##### from math import sqrt

# * loads the entire module (`math`) in memory if it's not already there
# * adds a reference to it in `sys.modules` with a key of `math`
# * adds the symbol `sqrt` to our current namespace referencing the `math.sqrt` function
# * it **does not** add the symbol `math` to our current namespace

# ##### from math import sqrt as r_sqrt

# * loads the entire module (`math`) in memory if it's not already there
# * adds a reference to it in `sys.modules` with a key of `math`
# * adds the symbol `r_sqrt` to our current namespace referencing the `math.sqrt` function
# * it **does not** add the symbol `math` to our current namespace

# ##### from math import *

# * loads the entire module (`math`) in memory if it's not already there
# * adds a reference to it in `sys.modules` with a key of `math`
# * adds symbols for all exported symbols in the `math` module directly to our name space (we'll see how what is exported from a module/package can be controlled using underscores or `__all__` later)
# * it **does not** add the symbol `math` to our current namespace

# As you can see, in **every** instance, the module is imported and a reference to it is added to `sys.modules`. The variants really have to do with what is injected into our current **namespace**: the module name, an alias to it, just the specified symbols from the module, or all the exported symbols from the module.

# #### Misconceptions

# This leads to the first misconception:

# "You should use
# `from math import sqrt, abs`
# rather than
# `import math`
# because that way you only import what you need and you're not having Python load the entire module?"

# For `math` that's just not true. In fact for any *simple* module.
# For *packages* that have subpackages, that may or may not be true - we'll see that later.

# Let's actually test this out.
# We have to be a little careful, because Jupyter imports a ton of modules and packages:
import sys
for key in sorted(sys.modules.keys()):
    print(key)


# so they're already loaded and in the `sys.modules` dictionary.
# Fortunately `cmath` is not one of them, so we'll use that one.
'cmath' in sys.modules


# Let's go ahead and just import a single symbol from `cmath`, the `exp` function:
from cmath import exp


# Now let's see if `cmath` and `exp` are in our module (global) namespace:
'cmath' in globals()

'exp' in globals()


# OK, so basically what that import did was create a symbol for `exp` in our namespace, but not for `cmath`.
# Does this mean that `cmath` was only "partially" loaded?

# How can Python "partially" load a (simple) module? How would it even know what to load up? Sure, maybe it could do some fancy kind of introspection and determine all the dependencies the symbols we are importing require. But it does not.
# It simply imports the entire module (using the techniques we have been covering in the last few videos)
# If we really want to partially load something, we would use a package, which, while still a `module` type, can be composed of several sub-packages. More on that later.

# In, fact let's look at it in `sys.modules`:
sys.modules['cmath']


# Yep, it's there...
# We can even get a handle to the `cmath` module:
cmath = sys.modules['cmath']

cmath


# And now we can use `cmath` just as if we had done
# `import cmath`
# But you'll note that in this case we did not import the module, we did `from cmath import exp` only.

# So we can use `exp` directly because of how we imported that specific symbol:
exp(2+3j)


# But we can also use the `cmath` module directly now that we retrieved it from `sys.modules`:
cmath.sqrt(1+1j)


# So, the **entire** `cmath` module was loaded when we ran `from cmath import exp`, not just a portion of it!

# The only thing that happened is that Python put `cmath` in `sys.modules`, but **did not** add a `cmath` symbol to our module namespace, and **only added** the function `exp` to our namespace.

# What about doing something like this:
# `from cmath import *`

# This is often frowned upon, and sometimes for good reason - but this is not a universal truth either.
# Let's see why, in our current context, it's maybe not such a good thing.
# First let's see what our global namespace looks like:
globals()


# Now let's do that import:
from cmath import *


# And let's see our namespace now:
globals()


# Some people say the namespace was "polluted". In a way I guess that's true, but it does mean I can now access **all** attributes in `cmath` without prefixing them with `cmath` all the time:
sqrt(2+2j)
pi
sin(2-3j)


# In and of itself, there's nothing wrong with that...
# But a couple of issues:

# The first one is that when I call `sin` just like that, someone reading my code does not immediately know where that function came from. Was it a function I implemented in my module? some other custom module? the `cmath` module? the `math` module?

# The second one is that you can run into serious problems if you also need to import the `math` module:

# Currently the `sqrt` symbol is the `cmath.sqrt` function:
sqrt
from math import *


# What just happened to the `sqrt` function that was in our namespace?
sqrt


# As you can see, the symbol `sqrt` in our namespace no longer refers to the `sqrt` function in `cmath` but rather to the one in `math`.
# It just got replaced by the `sqrt` function in the `math` module because it has the same name (`sqrt`).

# This is one of the reasons why `from ... import *` is sometimes frowned upon.
# But the same problem can happen if you use a `from` import this way:
from cmath import sqrt
from math import sqrt


# Same thing happened here, the `math.sqrt` function just clobbered the `cmath.sqrt` function.
# One option here is to use:
import cmath
import math
math.sqrt(2)
cmath.sqrt(2+2j)


# But Python also allows us to alias our imports using the `as` keyword.
# We can alias either the entire module, or just the symbols being imported from the module:
import math as r_math
import cmath as c_math
r_math
c_math
r_math.sqrt(2)
c_math.sqrt(2)


# By the way, this is the **exact** same result as doing:
import importlib
r_math = importlib.import_module('math')
c_math = importlib.import_module('cmath')
r_math
c_math


# We can also alias symbols from the imported module:
from math import sqrt as r_sqrt
from cmath import sqrt as c_sqrt
r_sqrt
c_sqrt


# Again, we can reproduce this using the following:
r_sqrt = importlib.import_module('math').sqrt
c_sqrt = importlib.import_module('cmath').sqrt
r_sqrt
c_sqrt


# At the end of the day, the module is always loaded and cached (`sys.modules`), these different variants of the `import` statement merely determine what symbols are added to our module (global) namespace. That's it.
# It's a little different for packages as we'll see later.

# #### Efficiency

# The final thing we need to look at is often mentioned in various blog posts and online discussions.
# `import variant #1` is more "efficient" than `import variant #2`
# Maybe so, but realistically by how much?
# Or even how the following is terribly wrong because it re-imports the `math` module **every** time `my_func` is called:
def my_func(a):
    import math
    return math.sqrt(a)


# From a readability standpoint, yes, that is **not** a good idea. Much better to put all your imports at the top of the module once in a location where any reader can easily see all your module dependencies.
# But as far as reloading the module, you should now understand that's absolutely not true. Instead, it has to do a dictionary lookup in the `sys.modules` dictionary, not reload the entire module after the first load has occurred!
# Dictionary lookups are blazingly fast in Python - so, yes, there is some overhead, but not as much as you may think.

# So, let's write some timing code to test these things and see how they compare.
# We shoudl consider both relative speed differences as well as absilute speed differences.
# If you try to optimize your code and end up reducing that code's speed by 50% that sounds good. But what if the original code ran in `1`s. Now it runs in `0.5`s. How long does the total program run? Down from `30`s to `29.5`s? Things are relative...
from time import perf_counter


# Yes, I'm using a `from` import - for readability and typing reasons. How many other modules are out there where I run the risk of clobbering `perf_counter`? I can't think of one. Certainly not in any imports I'm going to be using here. It's such a unique name, I feel pretty safe!

# I'm also going to write a small utility function that compares two timings to each other:
from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff_perc')
def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100

    timings = Timings(round(timing1, 1),
                     round(timing2, 1),
                     round(timing2 - timing1, 2),
                     round(rel_diff, 2))
    return timings


# ##### Timing using fully qualified `module.symbol`
test_repeats = 10_000_000

import math

start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')


# ##### Timing using a directly imported symbol name:
from math import sqrt

start = perf_counter()
for _ in range(test_repeats):
    sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')


# Let's see the relative and absolute time differences:
compare_timings(elapsed_fully_qualified, elapsed_direct_symbol)


# Definitely faster - but in absolute terms I really did not save a whole lot - over `10,000,000` iterations!

# ##### Timing using a function (fully qualified symbol)
import math

def func():
    math.sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_fully_qualified = end - start
print(f'Elapsed: {elapsed_func_fully_qualified}')

compare_timings(elapsed_fully_qualified, elapsed_func_fully_qualified)


# That was slower because of the function call overhead, but not by much in absolute terms considering I called `func()` `10,000,000` times!

# ##### Timing using a function (direct symbol)
from math import sqrt

def func():
    sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_direct_symbol = end - start
print(f'Elapsed: {elapsed_func_direct_symbol}')

compare_timings(elapsed_func_fully_qualified, elapsed_func_direct_symbol)


# Slower, but again not by much in absolute terms considering this was for `10,000,000` iterations.

# ##### Timing using a nested import (fully qualified symbol)
def func():
    import math
    math.sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_fully_qualified = end - start
print(f'Elapsed: {elapsed_nested_fully_qualified}')

compare_timings(elapsed_func_fully_qualified, elapsed_nested_fully_qualified)


# So definitely slower. But in absolute terms, for `10,000,000` iterations?

# ##### Timing using a nested import (direct symbol)
def func():
    from math import sqrt
    sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')

compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol)


# That was significantly slower! Even in absolute terms this is starting to get sloooow.

# So does this mean you should put imports inside functions?
# No, of course not - follow the convention, it makes code far more readable, and of course optimize your code only once you have identified the bottlenecks.
# Does this mean you shouldn't care at all about the performance of your code based on the import variants?
# Again, of course not - you absolutely should.
# But, there is absolutely no reason to re-write your code from
# `import math
# math.sqrt(2)`
# to
# `from math import sqrt
# sqrt(2)
# `
# for **speed** reasons if during the entire lifetime of your application you only call that function `100` times... or `10,000,000` times.
# Really depends on your circumstance - be aware of it, but don't try to optimize code until you know **where** you **need** to optimize!
# *[I've seen people refactor parts of their code for sub-second improvements, when, in fact, the largest bottleneck was that they were opening and closing database connections at every read and write instead of pooling connections or something like that]*

# And
# `from module import *`
# has its uses as we'll see later when we discuss packages.
# It's not evil, just not very safe - again depends on your circumstance.
