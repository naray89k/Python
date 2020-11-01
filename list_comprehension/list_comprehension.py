# -----------------------------------------------
# Level 1: Just Replace For-loops
full_name = "Yang Zhou"
characters = [char for char in full_name]
print(full_name)
print(characters)
# -----------------------------------------------

# -----------------------------------------------
# Level 2: Use the If Condition Smartly
Genius = ["Yang", "Tom", "Jerry", "Jack", "tom", "yang"]
L1 = [name for name in Genius if name.startswith('Y')]
L2 = [name for name in Genius if name.startswith('Y') or len(name) < 4]
L3 = [name for name in Genius if len(name) < 4 and name.islower()]
print(L1, L2, L3)
# -----------------------------------------------

# -----------------------------------------------
# Level 3: Use a More Complex Expression
Genius = ["Jerry", "Jack", "tom", "yang"]
L1 = [name.capitalize() for name in Genius]
print(L1)

Genius = ["Jerry", "Jack", "tom", "yang"]
L1 = [name if name.startswith('y') else 'Not Genius' for name in Genius]
print(L1)
# -----------------------------------------------


# -----------------------------------------------
# Level 4: Use Nested For-Loops to Handle Nested Iterables
Genius = ["Jerry", "Jack", "tom", "yang"]
L1 = [char for name in Genius for char in name]
print(L1)
# -----------------------------------------------


# -----------------------------------------------
# Level 5: Avoid Higher Order Functions for Readability
L = map(func, iterable)
# can be replaced to:
L = [func(a) for a in iterable]

L = filter(condition_func, iterable)
# can be converted to
L = [a for a in iterable if condition]
# -----------------------------------------------
