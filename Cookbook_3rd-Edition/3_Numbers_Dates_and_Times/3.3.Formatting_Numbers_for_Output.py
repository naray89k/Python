#!/usr/bin/env python
# coding: utf-8
x = 1234.56789

format(x, '0.2f')

format(x, '>10.1f')

format(x, '<10.1f')

format(x, '^10.1f')

format(x, '0,.1f')

format(x, 'e')

format(x, '0.2E')

'The value is {:0,.2f}'.format(x)

x

format(x, '0.1f')

format(-x, '0.1f')

#Pyton 3
swap_separators = { ord('.'):',', ord(','):'.' }
format(x, ',').translate(swap_separators)

'%0.2f'%x

'%10.1f'%x

'%-10.1f'%x



