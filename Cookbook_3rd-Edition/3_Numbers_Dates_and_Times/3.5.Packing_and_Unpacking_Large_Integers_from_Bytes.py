#!/usr/bin/env python
# coding: utf-8
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

len(data)

int.from_bytes(data, 'little')

int.from_bytes(data, 'big')

x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')

x.to_bytes(16, 'little')

data

hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo

x = 0x01020304
x.to_bytes(4, 'big')
x.to_bytes(4, 'little')

x = 523 ** 23

x

x.to_bytes(16,'little')

x.bit_length()

nbytes, rem = divmod(x.bit_length(),8)
if rem:
    nbytes += 1

x.to_bytes(nbytes, 'little')



