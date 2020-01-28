#!/usr/bin/env python
# coding: utf-8

# projectname/
#  README.txt
#  Doc/
#  documentation.txt
#  projectname/
#  __init__.py
#  foo.py
#  bar.py
#  utils/
#  __init__.py
#  spam.py
#  grok.py
#  examples/
#  helloworld.py
from distutils.core import setup
setup(name='projectname',
 version='1.0',
 author='Your Name',
 author_email='you@youraddress.com',
 url='http://www.you.com/projectname',
 packages=['projectname', 'projectname.utils'],
)



