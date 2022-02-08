def outer():
    x = 'Python'
    print(hex(id(x)))

    def inner():
        print(hex(id(x)))
        print('{0} Rocks !!!'.format(x))

    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)

# for elem in dir(fn):
#    print(elem)

# ============================================================
# Modifying free variables.
# ============================================================
def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


cntr_1 = counter()
print("First Counter:")
for e in range(1, 11):
    print(cntr_1())

# ============================================================
# Multiple instances of Closures .....
# ============================================================
# Every time we run a function, a new scope is created
# If that function creates a closure, a new closure is created every time as well.

cntr_2 = counter()
print("Second Counter:")
print(cntr_2())

# ============================================================
# Multiple instances of Closures .....
# ============================================================

