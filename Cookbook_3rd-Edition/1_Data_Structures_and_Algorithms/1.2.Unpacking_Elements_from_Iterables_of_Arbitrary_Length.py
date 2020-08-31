#!/usr/bin/env python
# coding: utf-8

# Python 3 "star expressions" can be used to address unpacking iterables of unknown or very large length.
# NB: This Jupyter Notebook uses Python 2 and so the Python 3 code is also adapted to Python 2 and the Python 3 code poses synax errors.
#First example if you need to find the average of the middle grades 
#Python 3 code
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

#Python 2 code
def py2_drop_first_last(grades):
    return (float(sum(grades[1:-1]))/(len(grades)))

float(py2_drop_first_last([1,2,3,4,5,6,7]))

#Python 3 code
record = ('Dave','dave@exmple.com','773-555-1212','847-555-1212')
name,email,*phone_numbers = record
name
email
phone_numbers

#Python 2 code
record = ('Dave','dave@exmple.com','773-555-1212','847-555-1212')
name = record[0]
email = record[1]
phone_numbers = record[-2:]

print(name)
print(email)
print(phone_numbers)

#Python 3 code

*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)
return avg_comparison(trailing_avg,current_qtr)

*trailing, current = [10,8,7,1,9,5,10,3]
trailing
current

#Python 2 code
sales_record = [10,8,7,1,9,5,10,3]
trailing = sales_record[0:-1]
current = sales_record[-1]
trailing_avg = sum(trailing)/(len(sales_record))
trailing, current

records = [
    ('foo', 1,2),
    ('bar','hello'),     
    ('foo',3,4),      
          ]

def do_foo(x,y):
    print('foo',x,y)
    
def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)|

#Python 2
records = [
    ('foo', 1,2),
    ('bar','hello'),     
    ('foo',3,4),      
          ]

def do_foo(x,y):
    print('foo',x,y)
    
def do_bar(s):
    print('bar',s)

for i in records:
    if i[0] == 'foo':
        do_foo(i[1],i[2])
    elif i[0] == 'bar':
        do_bar(i[1:])

#Python 3

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
uname
homedir
sh

#Python 2

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

list1 = line.split(':')
print(list1[0])
print(list1[-2])
print(list1[-1])

#Python 3

record = ('ACME', 50, 123.45, (12,18,2012))
name, *_, (*_,year) = record
name
year

#Python 2

record = ('ACME', 50, 123.45, (12,18,2012))
name = record[0]
year = record[-1][-1]

print(name)
print(year)

#Python 3 

items = [1,10,7,4,5,9]
head, *tail = items
head
tail

def sum2(head,tail):
    return head + sum(tail) if tail else head

sum2(head,tail)

#Python 2

items = [1,10,7,4,5,9]
head = items[0]
tail = items[1:]
head
tail

p = 0
for i in tail:
    p+=i
print(head+p)



