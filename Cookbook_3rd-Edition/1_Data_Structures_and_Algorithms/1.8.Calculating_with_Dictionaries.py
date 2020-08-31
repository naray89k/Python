#!/usr/bin/env python
# coding: utf-8
prices ={
     'ACME': 45.23,
     'AAPL': 612.78,
     'IBM': 205.55,
     'HPQ': 37.20,
     'FB': 10.75
}

zipped_file = (zip(prices.values(),prices.keys()))
prices_sorted = sorted(zipped_file)
min_price = min(zipped_file)
max_price = max(zipped_file)

print(prices_sorted)
print(min_price)
print(max_price)

min_price = prices_sorted[0]
max_price = prices_sorted[-1]

print(min_price)
print(max_price)

print(min(prices)
print(max(prices)

print(prices.values()
print 

for key, value in prices.items():
    if value == min(prices.values()):
        print key, value

print(min(prices, key = lambda k: prices[k])
print(max(prices, key = lambda j: prices[j])

min_value = prices[min(prices, key=lambda k:prices[k])]

print(min_value)

prices = {'AAA':45.23,'ZZZ':45.23}
print (min(zip(prices.values(),prices.keys())))
print (max(zip(prices.values(),prices.keys())))



