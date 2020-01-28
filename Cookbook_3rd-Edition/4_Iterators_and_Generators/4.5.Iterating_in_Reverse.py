#!/usr/bin/env python
# coding: utf-8
a = [1,2,3,4]
for x in reversed(a):
    print x

f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

class Countdown:
    def __init__(self, start):
        self.start = start
 
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
 
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

