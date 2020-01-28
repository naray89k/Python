#!/usr/bin/env python
# coding: utf-8
#Python 2

import io
s = io.StringIO()
int(s.write(u'Hello World\n'))

print('This is a test', file=s)

# Python 3
s = io.StringIO()
s.write('Hello World\n')

s.getvalue()

# Wrap a file interface around an existing string
s = io.StringIO(u'Hello\nWorld\n')
s.read(4)

s.read()

s = io.BytesIO()
s.write(b'binary data')
s.getvalue()



