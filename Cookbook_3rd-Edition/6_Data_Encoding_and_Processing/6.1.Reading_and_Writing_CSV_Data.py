#!/usr/bin/env python
# coding: utf-8
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:

from collections import namedtuple
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # Process row

import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
 ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
 ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
 ]


with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
 'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
 {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
 'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
 {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
 'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
 ]


with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        # process row

# Example of reading tab-separated values
with open('stock.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        # Process row

import re
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row

col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))

print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
 ('Change', float),
 ('Volume', int) ]


with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
        for key, conversion in field_types)
            print(row)

