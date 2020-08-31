#!/usr/bin/env python
# coding: utf-8
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr','joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub

sub.addr

sub.joined

len(sub)

addr, joined = sub
addr

joined

def compute_cost(records):
    total = 0
    for rec in records:
        total += rec[1] * rec[2]
    return total

from collections import namedtuple

Stock = namedtuple('Stock',['name','shares','prices'])

def compute_cost(records):
    total = 0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100,123.45)
s

s.shares = 75

s = s._replace(shares=75)
s

from collections import namedtuple

Stock = namedtuple('Stock',['name','shares','price','date','time'])

stock_prototype = Stock('',0,0.0,None,None)

print(stock_prototype)

#Python 3
def dict_to_stock(s):
    return stock_prototype._replace(**s)

dict_to_stock(s)



