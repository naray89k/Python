#!/usr/bin/env python
# coding: utf-8

# ### Python 3.6 - Underscores in Numeric Literals

# We can now intersperse underscores (`_`) in numeric literals.

# Makes things easier to read:
# `10_000_000` vs `10000000`

# Works for floats as well:
30_000.05


# But don't lead or end with the underscore!

# Works for hex numbers too:
0x_FF_FFFF, 0x_F_F_F_F_F_F


# (Just to show it does not matter how many digits are between the underscores)

# By the way, string formatting now supports that too - thousand separators for decimal integers and floats and every 4 digits for binary(`b`), octal(`o`), and hex(`x`, `X`).
'{:_}'.format(10000)

'{:_X}'.format(16777215)


# Works in string conversions too:
int('FF_FF', 16)

int('0b_1_0000_0000', 2)


# Pretty cool!
