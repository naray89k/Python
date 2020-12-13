#!/usr/bin/env python
# coding: utf-8
# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()


# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        pass
 # process line

# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)

# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)

with open('somefile.txt', 'rt', encoding='latin-1') as f:

f = open('somefile.txt', 'rt')
data = f.read()
f.close()

# Read with disabled newline translation
with open('somefile.txt', 'rt', newline='') as f:

# Newline translation enabled (the default)
f = open('hello.txt', 'rt')
f.read()

# Newline translation disabled
g = open('hello.txt', 'rt', newline='')
g.read()

f = open('sample.txt', 'rt', encoding='ascii')
f.read()

# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()


# Ignore bad chars entirely
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read()

