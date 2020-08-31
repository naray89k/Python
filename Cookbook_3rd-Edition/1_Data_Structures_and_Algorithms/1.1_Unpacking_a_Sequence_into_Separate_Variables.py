#!/usr/bin/env python
# coding: utf-8
p = (4,5)
x,y = p

print(x)
print(y)
print(x,y)

data = ['ACME',50, 91.1, (2012,12,21)]

name,share,price,date = data
print(name)
print(share)
print(price)
print(date)
print(name,share, price, date)

name,shares,price,(year,mon,day) = data
print(year)
print(mon)
print(day)
print (year,mon,day)


# NB: If there is a mismatch in the number of elements, an error will occur. Look Below.
p = (4,5)
x,y,z = p


# Unpacking works with any iterable in Python includings tuples, lists, strings, files, iterators, generators
s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(c)
print(d)
print(e)


# NB: even tho there is no synatc in discarding parts of the unpacked elements, you can use throwaway variables like '_' to discard unwated elements. 
# BE CAREFUL to pick variables that are not used anywhere in a code
data = ['ACME',50, 91.1, (2012,12,21)]

_,share,price,_ = data

print(share)
print(price)

print(share, price)



