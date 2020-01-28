#!/usr/bin/env python
# coding: utf-8
# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()


# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)


# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

import gzip

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

