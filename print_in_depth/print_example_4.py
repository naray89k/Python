#! /usr/bin/env python3

# Example 4.
# -----------

colors = ['red', 'blue', 'green']

print('Normal way')
for color in colors:
    print(color)
# red
# blue
# green

print('')

print('With \'end\' tweaked')
for color in colors:
    print(color, end=' and ')
# red and blue and green and

print('')
