#!/usr/bin/env python
# coding: utf-8
x = 1234
bin(x)

oct(x)

hex(x)

format(x, 'b')

format(x,'o')

format(x,'x')

x = -1234
format(x, 'b')

format(x,'x')

x = -1234
format(2**32 + x, 'b')

format(2**32 + x, 'x')

int('4d2', 16)

int('10011010010', 2)

import os
os.chmod('script.py', 0755)

os.chmod('script.py', 0o755)

