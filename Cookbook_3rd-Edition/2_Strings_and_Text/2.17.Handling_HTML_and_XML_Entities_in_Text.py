#!/usr/bin/env python
# coding: utf-8
# Python 3
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)

print(html.escape(s))

print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
s.encode('ascii', errors='xmlcharrefreplace')

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
unescape(t)



