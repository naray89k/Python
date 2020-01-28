#!/usr/bin/env python
# coding: utf-8
import webbrowser
webbrowser.open('http://www.python.org')

# Open the page in a new browser window
webbrowser.open_new('http://www.python.org')

# Open the page in a new browser tab
webbrowser.open_new_tab('http://www.python.org')

c = webbrowser.get('firefox')
c.open('http://www.python.org')

c.open_new_tab('http://docs.python.org')

