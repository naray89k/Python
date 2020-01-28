#! /usr/bin/env python3

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3]
avg = statistics.mean(data)
elements_above_average = list(filter(lambda x: x > avg, data))
elements_below_average = list(filter(lambda x: x < avg, data))

print(data)
print('Average:', avg)
print(elements_above_average)
print(elements_below_average)

# Another Example:
# ===============
# Remove missing data
countries = [ "India", "United Kingdom", "", "Argentina", "Brazil", "", "Chile", "Colombia", "", "Ecuador", "Singapore" ]
filtered_countries = list(filter(None, countries))
print(filtered_countries)
