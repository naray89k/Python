#!/usr/bin/env python
# coding: utf-8
s = 'pýtĥöñ\fis\tawesome\r\n'
s

# Python 3
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
}

a = s.translate(remap)
a

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
b

b.translate(cmb_chrs)

# Python 3
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'}
len(digitmap)

x = '\u0661\u0662\u0663'
x.translate(digitmap)

a

b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

