#!/usr/bin/env python
# coding: utf-8

# ### Random Choices

# How would you pick a random element from a list?
# You might be tempted to use the `random` library to pick a random index (integer) and use that random index to retrieve the element from the list (or more genrally sequence).
# Something like this:
import random


# I'm going to set a seed so we always generate the same random sequences:
random.seed(0)

l = [10, 20, 30, 40, 50, 60]

random_index = random.randrange(len(l))

l[random_index]


# So to do this 10 times we would write:
random.seed(0)
for i in range(10):
    print(l[random.randrange(len(l))])


# Although this certainly works, it's not very Pythonic. Instead we can use the `choice` function in the `random` module that picks a random element from any given sequence. (Again I'm going to set a seed so we can generate the same random sequence).
random.seed(0)
for _ in range(10):
    print(random.choice(l))


# Wasn't that much cleaner code?
# But still, there has to be a better way to generate 10 random choices without resorting to a "common" loop :-)

# The `random` module also has a `choices` method which allows us to choose multiple random choices (as opposed to `choice` which only picks one).

# The thing is, `choices` has a few more advanced features built in.
# Let's start with the basics.

# Suppose I want to choose n elements randomly from some sequence:
list_1 = list(range(1000))

random.choices(list_1, k=5)

for _ in range(5):
    print(random.choices(list_1, k=3))


# Now the thing about `choices` is that it does the selection *with replacement*. This means that the same item could show up more than once in the same call to `choices`. To see this, let's use a shorter list:
list_2 = ['a', 'b', 'c']

random.seed(0)
for _ in range(10):
    print(random.choices(list_2, k=2))


# As you can see we have some results that contain the same element twice.
# What this means, is that we can make the sample size *larger* than the population:
list_2

for _ in range(10):
    print(random.choices(list_2, k=5))


# In addition, we can also specify a weight for each item in the population. This essentially allows us to have certain items be picked more often than others. The weight list must be the same length as the population.
weights_2 = [10, 1, 1]

for _ in range(10):
    print(random.choices(list_2, k=5, weights=weights_2))


# As you can see, we see a whole lot more of `a` than the other characters.

# We can skew the results even more, simply by increasing the weight for `a`:
weights_2 = [100, 1, 1]

for _ in range(10):
    print(random.choices(list_2, k=5, weights=weights_2))


# Let's see if we can count the frequency of each element that is returned by `choices`.
# To do that we are going to use a comprehension. While we're at it we'll calculate also the relative frequency of each item.
from collections import namedtuple

Freq = namedtuple('Freq', 'count freq')

def freq_counts(list_):
    total = len(list_)
    return {k: Freq(list_.count(k), 100 * list_.count(k)/total) for k in set(list_)}

freq_counts(random.choices(list_2, k=1000))


# As you can see, the distribution is pretty even. Now let's skew thing a little:
random.seed(0)
freq_counts(random.choices(list_2, k=1_000, weights=(8, 1, 1)))


# And the relative frequency of `a` is:

# Which matches what we would expect since we gave `a` a weight of `8` out of a total sum of weights of `10` - so 80%.

# Of course, the more elements we pick, the closer this value should get to the theoretical:
freq_counts(random.choices(list_2, k=10_000, weights=(8, 1, 1)))


# You can also specify the weights as cumulative weights:
# So instead of `8, 1, 1` as weights, we could provide cumulative weights as `8, 9, 10`:
random.seed(0)
freq_counts(random.choices(list_2, k=1_000, cum_weights = (8, 9, 10)))


# And we get the same thing.

# As a bonus, how would we go about generating 50 evenly distributed random numbers between 0 and 100 (inclusive) say?

# We could certainly use the `randint` function and put that into a loop 50 times:
l = []
for _ in range(50):
    l.append(random.randrange(101))
print(l)


# But we could just use the `choices` method instead with a range(101):
l = random.choices(range(101), k=50)
print(l)


# Only caution here is if you are generating random things on multiple threads - in which case you don't know when what thread is going to run and in that case you very well may end up with different random results from the various threads from run to run - even if you use a specific seed.

# Here's one practical application of being able to skew random selections.
# Let's say you want to know what's more efficient - guarding a divide by zero exception using a LBYL (look before you leap) approach, or EAFP (easier to ask for forgiveness than permission):
from time import perf_counter

denominators = random.choices([0, 1], k=1_000_000)

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')   

start = perf_counter()
for denominator in denominators:
    try:
        10 / denominator
    except ZeroDivisionError:
        continue

end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')


# As we can see it looks like the `try... except...` appeoach is slower.
# But in reality, we expect that a zero will only occur 10% of the time.
# So now we can test this using a skewed set of random denominators:
denominators = random.choices([0, 1], k=1_000_000, weights=[1, 9])

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
        
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')



