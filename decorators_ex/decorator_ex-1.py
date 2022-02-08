# Decorator Function.
def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


# METHOD-1
# def add(a, b=0):
#    return a + b

# add = counter(add)

# METHOD-2
@counter
def add(a, b=0):
    return a + b


result = add(1, 2)
print(result)
result = add(3, 4)
print(result)

# README.
# In general a decorator function
# 1. takes a function as an argument.
# 2. returns a closure
# 3. the closure usually accepts any combination of parameters.
# 4. some code in the inner function (closure)
# 5. the closure function calls the original function using the arguments passed to the closure
# 6. returns whatever is returned by that function call.
