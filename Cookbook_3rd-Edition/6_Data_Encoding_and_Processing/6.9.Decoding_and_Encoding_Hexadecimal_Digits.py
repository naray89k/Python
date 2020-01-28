#!/usr/bin/env python
# coding: utf-8
# Initial byte string
s = b'hello'


# Encode as hex
import binascii
h = binascii.b2a_hex(s)
h

# Decode back to bytes
binascii.a2b_hex(h)

import base64
h = base64.b16encode(s)
h

base64.b16decode(h)

h = base64.b16encode(s)
print(h)

print(h.decode('ascii'))



