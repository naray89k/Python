#!/usr/bin/env python
# coding: utf-8
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days

c.seconds

c.seconds/3600

c.total_seconds()/3600

from datetime import datetime
a = datetime(2012,9,23)
print(a + timedelta(days=10))

b = datetime(2012,12,21)
d = b -a
d.days

now = datetime.today()
print(now)

print(now + timedelta(minutes=10))

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
a - b

(a-b).days

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
(c-d).days

a = datetime(2012, 9, 23)
a + timedelta(months=1)

from dateutil.relativedelta import relativedelta
a + relativedelta(months=+1)

a + relativedelta(months=+4)

b = datetime(2012, 12, 21)
d = b - a
d

d = relativedelta(b,a)
d

d.months

d.days



