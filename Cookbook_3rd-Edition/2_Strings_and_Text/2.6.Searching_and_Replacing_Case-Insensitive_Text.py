#!/usr/bin/env python
# coding: utf-8
import re
text = 'UPPER PYTHON, lower python, Mixed Python'

re.findall('python', text, flags=re.IGNORECASE)

re.sub('python', 'snake', text, flags=re.IGNORECASE)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)



