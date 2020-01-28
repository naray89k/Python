#!/usr/bin/env python
# coding: utf-8
import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]

print heapq.nlargest(len(nums),nums)
print heapq.nsmallest(len(nums),nums)

portfolio = [
     {'name': 'IBM', 'shares': 100, 'price': 91.1},
     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
     {'name': 'FB', 'shares': 200, 'price': 21.09},
     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
     {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(len(portfolio), portfolio, key=lambda k: k['price'])
expensive = heapq.nlargest(len(portfolio), portfolio, key=lambda k: k['price'])

print cheap
print expensive

nums = [1,8,2,23,7,-4,18,23,42,37,2]

import heapq
heap = list(nums)
heapq.heapify(heap)
heap

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
heap



