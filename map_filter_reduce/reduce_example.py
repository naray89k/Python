#! /usr/bin/env python3

from functools import reduce

# Multiply all numbers in a list.

data = list(range(1, 11))
multiplier = lambda x, y: x*y
adder = lambda x, y: x+y
product_of_list_elems = reduce(multiplier, data)
sum_of_list_elems = reduce(adder, data)

print(data)
print(product_of_list_elems)
print(sum_of_list_elems)

### Explanation.
# Reduce function takes first two elements of a list and process them as per function passed,
# then in the next iteration, the output and third element in the list will be processed in the same way as above.
# The process will continue until it reaches the end element in list.
