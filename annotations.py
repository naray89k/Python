#! /usr/bin/env python3
import re

def power_func(a:int, b:int = 2) -> "a to the power of b":
    """Short summary.

    Parameters
    ----------
    a : int
        Description of parameter `a`.
    b : int
        Description of parameter `b`.

    Returns
    -------
    "a to the power of b"
        Description of returned object.

    """
    return a ** b


print(power_func(2))

print(power_func.__doc__)
print(power_func.__annotations__)
