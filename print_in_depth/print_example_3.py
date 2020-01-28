#! /usr/bin/env python3

# Example 3.
# -----------

class MyInteger:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value + 3)

i = MyInteger(4)
print(i) # -> output: 7

# str(x) is used to convert the int to a string.
# When printing an object of MyInteger it will always
# print its value incremented by 3. In the __repr__(self)
# method of an object you can define how it is to be printed.
