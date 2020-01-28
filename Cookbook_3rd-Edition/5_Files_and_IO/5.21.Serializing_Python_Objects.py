#!/usr/bin/env python
# coding: utf-8
import pickle
data = ... # Some Python object
f = open('somefile', 'wb')
pickle.dump(data, f)

s = pickle.dumps(data)

# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)


# Restore from a string
data = pickle.loads(s)

import pickle
f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
pickle.load(f)

pickle.load(f)

pickle.load(f)

import math
import pickle.
pickle.dumps(math.cos)

class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
 
    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)

import countdown
c = countdown.Countdown(30)
T-minus 30

# After a few moments
f = open('cstate.p', 'wb')
import pickle
pickle.dump(c, f)
f.close()

f = open('cstate.p', 'rb')
pickle.load(f)

