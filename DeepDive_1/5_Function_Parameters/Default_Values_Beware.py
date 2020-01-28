#!/usr/bin/env python
# coding: utf-8

# ### Default Values - Beware!
from datetime import datetime
print(datetime.utcnow())

def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

log('message 1')
log('message 2', dt='2001-01-01 00:00:00')
log('message 3')
log('message 4')


# As you can see, the default for **dt** is calculated when the function is **defined** and is **NOT** re-evaluated when the function is called.
# #### Solution Pattern
# Here is one pattern we can use to achieve the desired result:
# We actually set the default to None - this makes the argument optional, and we can then test for None **inside** the function and default to the current time if it is None.
def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # above is equivalent to:
    #if not dt:
    #    dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log('message 1')
log('message 2')
log('message 3', dt='2001-01-01 00:00:00')
log('message 4')
