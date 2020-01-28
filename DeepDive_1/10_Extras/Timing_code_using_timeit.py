#!/usr/bin/env python
# coding: utf-8

# #### Timing code using timeit

# When we were looking at decorators we wrote a timing decorator. It could even take a number of repititions as a parameter. This can be handy to time functions directly in your code without affecting the result of the function. But it wrote the results out to the console, and sometimes we just want to access the timing data right inside our Python code.
# The `timeit` module in Python is an alternative that works well for some things. It is a little more complicated to use because it runs 'outside' of our local namespace, and you have to pass just small snippets of code to it (well you pass multi-line chunks of code, but it gets tedious), and you also have to make it aware of you global or local scope if that's needed by the code you want to time. One thing it does that we did not do was *temporarily disable* the garbage collector. Still, there are a lot of pitfalls to benchmarking, and this approach like ours, is good enough for most cases. YMMV.
# It has the advantage that it can also be run directly from the command line.
# Let's take a look at it.
from timeit import timeit


# We look at the `timeit` function. There are a few others but this is the main one and the remaining are slight variations that you may find useful, so check out the Python docs for more info.

# Basically the `timeit` function needs to know a few things:
# - the Python statement to run (the **stmt** argument)
# - how many times to run the same code (the **number** argument - watch out, the default is `1_000_000` times!)
# - any setup code (like imports) (the **setup** argument)
# - an optional scope that acts like a global scope to the statement (the **globals** argument)
# It will then execute the test `number` of times and return the **total** time elapsed (not an average per test).

# Let's start with a simple example, where we want to time how long it takes to run the `sqrt` function in the `math` module using two different ways of importing it:

# The first case we want to time is the following:
import math
math.sqrt(2)


# vs
from math import sqrt
sqrt(2)


# As you can see in the first example we have to specify `name.sqrt` every time we want to call the `sqrt` function. Is there a time difference between those two approaches?

# Let's timeit!
timeit(stmt='math.sqrt(2)')


# UhOh... we get an exception. Basically `timeit` has no idea what the `math` module is! Remember what I said that it runs inside its own name space?

# We can fix this in three ways:

# **First** way we can simply add the import to the statement we want to time.
timeit(stmt = 'import math\nmath.sqrt(2)')


# This is bad for two reasons: readability obviously, but also the timing is now going to include timing the `import math` statement **every time** as well. That's not how our imports work in Python. We import once and then use that imported module over and over again. 

# **Second** way is to use the `setup` argument - basically that allows us to setup the runtime environment of whatever code snippet we want to run. That setup code is only run once, not for every test:
timeit(stmt = 'math.sqrt(2)', setup='import math')


# As you can see this ran faster than importing at every test.

# **Third** way is to provide `timeit` with a global namespace that already contains the import - as we have in our case. Our `global` namespace already has the import:
timeit(stmt='math.sqrt(2)', globals=globals())


# As you can see that was a little less efficient (but what's about `0.01` seconds over `1_000_000` repetitions between friends...)

# So let's go with the `setup` approach and now time the difference between using the two import styles:
result_1 = timeit(stmt='math.sqrt(2)', setup='import math')
result_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')
print(f'Result 1 = {result_1}')
print(f'Result 2 = {result_2}')


# As you can see the `from math import sqrt` was slightly more efficient. But again, what's a about `0.4` seconds over `1_000_000` iterations. 
# If that's what you're optimizing before you even profile your application you're doing things wrong!
# Explicit is better than implicit.
# So when someone sees `math.sqrt` they know `sqrt` comes from the `math` module. If they see `sqrt` they have to look at your imports to double check which module `sqrt` came from.
# If the module name is long and you don't want to always type it, you can always alias it. Or use the `from` style of import. Whatever reads best since optimization is not really a concern at that point.

# One last thing, what if the statement(s) you want to time require something from the scope in which it is running? How do you "pass" that variable to the `timeit` statement?
# That's where the `globals` argument comes in - we already saw it in action for the imports, but the `globals()` and `locals()` functions can reference the global and local name spaces.
globals()

locals()


# Let's use globals first:
import random

l = random.choices(list('python'), k=500)


# The variable `l` is now in our global name space.
'l' in globals()


# And technically in our local name space too:
'l' in locals()

timeit(stmt='random.choice(l)', setup='import random', globals=globals())


# As you can see the statement was able to access `l` from the `globals()` that as passed to the `global` argument.

# Sometimes though you may have to use the local namespace, for exampele inside a function:
def random_choices():
    randoms = random.choices(list('python'), k=500)
    
    return timeit(stmt='random.choice(randoms)', 
                  setup='import random', 
                  globals=locals())

random_choices()


# I hope you saw that running the code using a local `randoms` ran slightly faster than using it from the global scope!
# We'll come back to that in a later video, but in fact running code from the global namespace (i.e. at the module level) is slightly slower in general than running it in a local namespace (i.e. inside a function).

# If we had passed it `globals()` instead it would not have worked since `randoms` is not in the global namespace:
'randoms' in globals()

def random_choices():
    randoms = random.choices(list('python'), k=500)
    return timeit(stmt='random.choice(randoms)',
                  setup='import random',
                  globals=globals())

random_choices()


# One more thing to point out is that functions defined at the module level are actually in our global namespace as well:
def pick_random(lst):
    return random.choice(lst)

'pick_random' in globals()


# This means that technically we can write the function we want to time in our global/local scope, and pass the scope in and then reference the function from that scope in our statement. It will be slower though since it has to find the function in the scope first - but you could do it to test relative performance differences:
timeit(stmt='pick_random(l)', globals=globals())


# And there you go, `timeit` was able to access both `pick_random` and the variable `l`.
