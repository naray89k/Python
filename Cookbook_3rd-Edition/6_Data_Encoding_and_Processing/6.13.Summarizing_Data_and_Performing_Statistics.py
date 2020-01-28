#!/usr/bin/env python
# coding: utf-8
import pandas
# Read a CSV file, skipping last line
rats = pandas.read_csv('rats.csv', skip_footer=1)
rats

# Investigate range of values for a certain field
rats['Current Activity'].unique()

# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
len(crew_dispatched)

# Find 10 most rat-infested ZIP codes in Chicago
crew_dispatched['ZIP Code'].value_counts()[:10]

# Group by completion date
dates = crew_dispatched.groupby('Completion Date')

len(dates)

# Determine counts on each day
date_counts = dates.size()
date_counts[0:10]

# Sort the counts
date_counts.sort()
date_counts[-10:]

