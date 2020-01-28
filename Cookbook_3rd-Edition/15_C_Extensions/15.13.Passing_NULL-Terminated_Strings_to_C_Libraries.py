#!/usr/bin/env python
# coding: utf-8
print_chars(b'Hello World')

print_chars(b'Hello\x00World')

print_chars('Hello World')

print_chars('Hello World')

print_chars('Spicy Jalape\u00f1o') # Note: UTF-8 encoding

print_chars('Hello\x00World')

print_chars(b'Hello World')

import sys
s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s)

print_chars(s) # Passing string

sys.getsizeof(s) 

import sys
s = 'Spicy Jalape\u00f1o'
sys.getsizeof(s)

print_chars(s)

sys.getsizeof(s)

import ctypes
lib = ctypes.cdll.LoadLibrary("./libsample.so")
print_chars = lib.print_chars
print_chars.argtypes = (ctypes.c_char_p,)
print_chars(b'Hello World')

print_chars(b'Hello\x00World')

print_chars('Hello World')

print_chars('Hello World'.encode('utf-8'))

