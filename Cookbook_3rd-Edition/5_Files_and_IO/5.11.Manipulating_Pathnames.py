#!/usr/bin/env python
# coding: utf-8
import os
path = '/Users/beazley/Data/data.csv'

# Get the last component of the path
os.path.basename(path)


# Get the directory name
os.path.dirname(path)

# Join path components together
os.path.join('tmp', 'data', os.path.basename(path))

# Expand the user's home directory
path = '~/Data/data.csv'
os.path.expanduser(path)

# Split the file extension
os.path.splitext(path)

