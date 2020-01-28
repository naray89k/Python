#!/usr/bin/env python
# coding: utf-8

# ### Decimals
import decimal

from decimal import Decimal


# Decimals have context, that can be used to specify rounding and precision (amongst other things)
# Contexts can be local (temporary contexts) or global (default)
# #### Global Context
g_ctx  = decimal.getcontext()
g_ctx.prec
g_ctx.rounding


# We can change settings in the global context:
g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP


# And if we read this back directly from the global context:
decimal.getcontext().prec
decimal.getcontext().rounding

# we see that the global context was indeed changed.

# #### Local Context

# The ``localcontext()`` function will return a context manager that we can use with a ``with`` statement:
with decimal.localcontext() as ctx:
    print(ctx.prec)
    print(ctx.rounding)


# Since no argument was specified in the ``localcontext()`` call, it provides us a context manager that uses a copy of the global context.
# Modifying the local context has no effect on the global context
with decimal.localcontext() as ctx:
    ctx.prec = 10
    print('local prec = {0}, global prec = {1}'.format(ctx.prec, g_ctx.prec))

# #### Rounding
decimal.getcontext().rounding

# The rounding mechanism is ROUND_HALF_UP because we set the global context to that earlier in this notebook. Note that normally the default is ROUND_HALF_EVEN.
# So we first reset our global context rounding to that:
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

# Let's change the rounding mechanism in the global context to ROUND_HALF_UP:
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

# As you may have realized, changing the global context is a pain 
# if you need to constantly switch between different precisions and rounding algorithms. 
# Also, it could introduce bugs if you forget that you changed the global context somewhere further up in your module.
# For this reason, it is usually better to use a local context manager instead:
# First we reset our global context rounding to the default:
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
print(round(x, 1), round(y, 1))

