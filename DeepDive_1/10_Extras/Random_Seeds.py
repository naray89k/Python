#!/usr/bin/env python
# coding: utf-8

# ### Random Seeds

# The `random` module provides a variety of functions related to (pseudo) random numbers.
# The problem when you use random numbers in your code is that it can be difficult to debug because the same random number sequence is not the same from run to run of your program. If your code fails somewhere in the middle of a run it is difficult to make the problem **repeatable**. Debugging intermittent and non-repeatable failures is one of the worst things to do!
# Fortunately, when using the `random` module, we can set the `seed` for the random underlying random number generator.
# Random numbers are not truly random - they are generated in such a way that the numbers *appear* random and evenly distributed, but in fact they are being generated using a specific algorithm.
# That algorithm depends on a **seed** value. That seed value will determine the exact sequence of randomly generated numbers (so as you can see, it's not truly random). Setting different seeds will result in different random sequences, but setting the seed to the same value will result in the same sequence being generated.
# By default, the seed uses the system time, hence every time you run your program a different seed is set. But we can easily set the seed to something specific - very useful for debugging purposes.
import random

for _ in range(10):
    print(random.randint(10, 20), random.random())

for _ in range(10):
    print(random.randint(10, 20), random.random())


# As you can see the sequence of numbers is not the same (and even restarting the kernel will result in different numbers).

# We can set the **seed** as follows:
random.seed(0)
for i in range(10):
    print(random.randint(10, 20), random.random())


# If we run this code again, the sequence will still be different:
for i in range(10):
    print(random.randint(10, 20), random.random())


# Instead what we have to do is reset the seed (which happens if you set the seed to a specific number at the start of running your program - then evey random number generated will be repeatable from run to run).
# Here, we just need to reset the seed before running that loop to get the same effect:
random.seed(0)
for i in range(20):
    print(random.randint(10, 20), random.random())

random.seed(0)
for i in range(20):
    print(random.randint(10, 20), random.random())


# As you can see, the sequence of random numbers generated is now the same every time.

# What's interesting is that even functions like `shuffle` will shuffle in the same order!
# Let's see this:
def generate_random_stuff(seed=None):
    random.seed(seed)
    results = []
    
    # randint will generate the same sequence (for same seed)
    for _ in range(5):
        results.append(random.randint(0, 5))
    
    # even shuffling generates in the same way (for same seed)
    characters = ['a', 'b', 'c']
    random.shuffle(characters)
    results.append(characters)
    
    # same with the Gaussian distribution
    for _ in range(5):
        results.append(random.gauss(0, 1))
        
    return results

print(generate_random_stuff())

print(generate_random_stuff())


# Now let's use a seed value:
print(generate_random_stuff(0))

print(generate_random_stuff(0))


# As long as we use the same seed value the results are repeatable. But if we set different seed values the sequences will be different (but still be the same for the same seed):
print(generate_random_stuff(100))

print(generate_random_stuff(100))


# Lastly let's see how we would calculate the frequency of randomly generated integers, just to see how even the distribution is.
# Basically, given a sequence of random integers, we are going to create a dictionary that contains the integers as keys, and the values will the frequency of each:
def freq_analysis(lst):
    return {k: lst.count(k) for k in set(lst)}

lst = [random.randint(0, 10) for _ in range(100)]

print(lst)

random.seed(0)
freq_analysis(lst)

random.seed(0)
freq_analysis([random.randint(0, 10) for _ in range(1_000_000)])


# Of course, it usually pays to know what's in the standard library :-)
# The collections library has a Counter class that can be used to do this precise thing!
from collections import Counter

random.seed(0)
Counter([random.randint(0, 10) for _ in range(1_000_000)])



