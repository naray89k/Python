#!/usr/bin/env python
# coding: utf-8
text = 'Hello World'
text.ljust(20)

text.rjust(20)

text.center(20)

text.rjust(20,'=')

text.center(20,'*')

format(text, '>20')

format(text,'<20')

format(text, '^20')

format(text, '=>20s')

format(text, '*^20s')

'{:>10s}{:>10s}'.format('Hello','World')

x = 1.2345
format(x, '>10')

format(x, '^10.2f')

'%-20s'%text

'%20s'%text



