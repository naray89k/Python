#!/usr/bin/env python
# coding: utf-8

# ### Random Samples

# I just want to show you a variant on `random.choices` that we saw in the previous video.

# `choices` chooses `k` random elements from some sequence, **with replacement**.
# This means we could create a random selection containing more elements than we started off with:
import random

random.choices(list('abc'), k=10)


# Sometimes however, we do not want that replacement - instead we want a population sample (so once an element has been randomly selected, it cannot be selected again).
# This is where the `sample` function comes in - it does exactly that. Of course, we can no longer pick more elements than we have in our population. Also, picking a sample equal in size to the population basically returns a "shuffled" population.
l = range(20)

random.sample(l, k=10)


# We can even set the sample size equal to the population size:
random.sample(l, k=20)


# But no larger than the population size:
random.sample(l, 50)


# Also worth pointing out is that if you set a specific seed, you will get repeatability of your sample selection:
random.seed(0)
random.sample(l, k=5)

random.seed(0)
random.sample(l, k=5)


# Let's see how we might use this to select some cards from a deck - obviously we don't want replacement here - once a card has ben picked from a deck it's no longer available for a second random pick.
suits = 'C', 'D', 'H', 'A'
ranks = tuple(range(2,11)) + tuple('JQKA')

suits

ranks


# Now we have to combine suits and ranks to form a deck.
deck = [str(rank) + suit for suit in suits for rank in ranks]

print(deck)


# Let's import `Counter` from the collections module to make sure we have no repitition when we pull a sample vs when we use `choices`.
from collections import Counter

Counter(random.sample(deck, k=20))


# But if we used `choices` most likely we'll get some repetitions:
Counter(random.choices(deck, k=20))

