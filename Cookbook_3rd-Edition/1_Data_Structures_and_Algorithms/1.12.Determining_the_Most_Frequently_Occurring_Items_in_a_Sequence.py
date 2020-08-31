#!/usr/bin/env python
# coding: utf-8
from collections import Counter
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)

word_counts['eyes']

word_counts.update(morewords)
print(word_counts)

a = Counter(words)
b = Counter(morewords)
a

b

c = a+b
c

d = a - b
d



