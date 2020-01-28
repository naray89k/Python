#!/usr/bin/env python
# coding: utf-8

# ### Named Tuples - Application - Returning Multiple Values

# We already know that we can easily return multiple values from a function by using a tuple:
from random import randint, random

def random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

random_color()


# So of course, we could call the function this and unpack the results at the same time:
red, green, blue, alpha = random_color()
print(f'red={red}, green={green}, blue={blue}, alpha={alpha}')


# But it might be nicer to use a named tuple:
from collections import namedtuple
Color = namedtuple('Color', 'red green blue alpha')

def random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()
color.red
color
