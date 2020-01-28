#!/usr/bin/env python
# coding: utf-8
def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise

example()

try:
    
except Exception as e:
    # Process exception information in some way

    # Propagate the exception
    raise

