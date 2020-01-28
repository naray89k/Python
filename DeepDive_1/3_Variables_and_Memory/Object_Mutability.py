#!/usr/bin/env python
# coding: utf-8

# ## Object Mutability
# Certain Python built-in object types (aka data types) are **mutable**.
# That is, the internal contents (state) of the object in memory can be modified.
my_list = [1, 2, 3]
print(my_list)
print(hex(id(my_list)))

my_list.append(4)
print(my_list)
print(hex(id(my_list)))

# As you can see, the memory address of *my_list* has **not** changed.
# But, the **contents** of *my_list* has changed from *[1, 2, 3]* to *[1, 2, 3, 4]*.

# On the other hand, consider this:
my_list_1 = [1, 2, 3]
print(my_list_1)
print(hex(id(my_list_1)))

my_list_1 = my_list_1 + [4]
print(my_list_1)
print(hex(id(my_list_1)))


# Notice here that the memory address of *my_list_1* **did** change.
# This is because concatenating two lists objects *my_list_1* and *[4]* did not modify the contents of *my_list_1*.
# instead it created a new list object and re-assigned *my_list_1* to reference this new object.
# Similarly with **dictionary** objects that are also **mutable** types.
my_dict = dict(key1='value 1')
print(my_dict)
print(hex(id(my_dict)))

my_dict['key1'] = 'modified value 1'
print(my_dict)
print(hex(id(my_dict)))

my_dict['key2'] = 'value 2'
print(my_dict)
print(hex(id(my_dict)))


# Once again we see that while we are modifying the **contents** of the dictionary, the memory address of *my_dict* has not changed.
# Now consider the immutable sequence type: **tuple**
# The tuple is immutable, so elements cannot be added, removed or replaced.
t = (1, 2, 3)


# This tuple will **never** change at all. It has three elements, the integers 1, 2, and 3. 
# This will remain the case as long as **t**'s reference is not changed.
# But, consider the following tuple:
a = [1, 2]
b = [3, 4]
t = (a, b)


# Now, **t** is still immutable, i.e. it contains a reference to the object **a** and the object **b**.
# **That** will never change as long as **t**'s reference is not re-assigned.
# **However**, the elements **a** and **b** are, themselves, mutable.
a.append(3)
b.append(5)
print(t)


# Observe that the contents of **a** and **b** **did** change!
# So immutability can be a little more subtle than just thinking something can never change. 
# The tuple **t** did **not** change - it contains two elements, that are the references **a** and **b**.
# And that will not change. But, because the referenced elements are mutable themselves, it appears as though the tuple has changed.
# It hasn't though - that distinction is subtle but important to understand!
