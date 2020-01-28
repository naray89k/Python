#! /usr/bin/env python3

from time import perf_counter, sleep

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()
sleep(100)
print(t1())
