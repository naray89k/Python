#! /usr/bin/env python3

import math

def area(r):
    """ Given radius r the function returns area of circle """
    return math.pi * (r**2)

radii = [ 2, 5, 8, 8.9, 9.8 ]

# Method 1:
areas = []
for radius in radii:
    areas.append(area(radius))
print(areas)

# Method 2:
areas = list(map(area, radii))
print(areas)

# ====== Another Example ======
temps = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19),
         ('Los Angeles', 26), ('Tokyo', 27), ('New York', 28),
         ('London', 22), ('Beijing', 32)]
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

temps_in_fahrenheit = list(map(c_to_f,temps))
print(temps)
print(temps_in_fahrenheit)

### Explanation.
# Reduce function takes elements of the list passed one by one and process it according the function passed and stores it as a result.
