#!/usr/bin/env python
# coding: utf-8

# ### Reloading Modules

# Reloading modules is something you may find yourself wanting to do if you modify the code for a module while your program is running.

# Although you technically can do so, and I'll show you two ways of doing it, it's not recommended. Let me show you how to do it first, and then the pitfalls with both methods.
# The safest is just to make your code changes, and restart your app.
# Even if you are trying to monkey patch (change at run-time) a code module and you want everyone who uses that module to "see" the change, they very well may not, depending on how they are accessing your module.

# As usual, working with external modules in Jupyter is not the easiest thing in the world, so I'm just going to create simple modules right from inside the notebook. You can just create files in the same folder as your notebook/main app instead.
import os

def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py.
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs.
    '''

    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")

create_module_file('test', k1=10, k2='python')


# This should have resulted in the creation of a file named `test.py` in your notebook/project directory that should look like this:
# `# test.py`
# `print('running test.py...')`
# ``def print_values():
# 	print('k1', '10')
# 	print('k2', 'python')
# ``

# Now let's go ahead and import it using a plain `import`:
import test
test


# And we can now call the `print_values` function:
test.print_values()


# Now suppose, we modify the module by adding an extra key:
create_module_file('test', k1=10, k2='python', k3='cheese')
test.print_values()


# Nope, nothing changed...

# Maybe we can just re-import it?? You shoudl know the answer to that one...
import test
test.print_values()
id(test)


# The module object is the same one we initially loaded - our namespace and `sys.modules` still points to that old one. Somehow we have to force Python to *reload* the module.

# At this point, I hope you're thinking "let's just remove it from `sys.modules`, this way Python will not see it in the cache and rerun the import.
# That's a good idea - let's try that.
import sys
del sys.modules['test']
import test
test.print_values()


# and, in fact, the `id` has also changed:
id(test)


# That worked!

# But here's the problem with that approach.
# Suppose some other module in your program has already loaded that module using
# `import test`.
# What is in their namespace? A variable (symbol) called `test` that points to which object? The one that was first loaded, not the second one we just put back into the `sys.modules` dict.
# In other words, they have no idea the module changed and they'll just keep using the old object at the original memory address.

# Fortunately, `importlib` has a way to reload the contents of the module object without affecting the memory address.
# That is already much better.
# Let's try it:
id(test)
test.print_values()
create_module_file('test', k1=10, k2='python',
                   k3='cheese', k4='parrots')
import importlib
importlib.reload(test)


# As we can see the module was executed...

# what about the `id`?
id(test)


# Stayed the same...

# So now, let's call that function:
test.print_values()


# As you can see, we have the correct output. And we did not have to reimport the module, which means any other module that had imported the old object, now is going to automatically be using the new "version" of the same object (same memory address)

# So, all's well that ends well...
# Not quite. :-)

# Consider this example instead, were we use a `from` style import:
create_module_file('test2', k1='python')
from test2 import print_values
print_values()


# Works great.
# What's the `id` of `print_values`?
id(print_values)


# Now let's modify `test2.py`:
create_module_file('test2', k1='python', k2='cheese')


# And reload it using `importlib.reload`:
importlib.reload(test2)


# Ok, so we don't have `test2` in our namespace... Easy enough, let's import it directly (or get it out of `sys.modules`):
import test2
test2.print_values()
id(test2.print_values)
id(print_values)


# Now let's try the reload:
importlib.reload(test2)


# OK, the module was re-imported...

# Now let's run the `print_values` function:
test2.print_values()


# But remember how we actually imported `print_values` from `test2`?
print_values()


# Ouch - that's not right!

# Let's look at the `id`s of those two functions, and compare them to what we had before we ran the reload:
id(test2.print_values)
id(print_values)


# As you can see the `test2.print_values` function is a new object, but `print_values` **still** points to the old function that exists in the first "version" of `test2`.

# And that is why reloading is just not safe.
# If someone using your module binds directly to an attribute in your module, either via how they import:
# `from test2 import print_values`
# or even by doing something like this:
# `pv = test2.print_values`
# their binding is now set to a specific memory address.
# When you reload the module, the object `test2` has ben mutated, and the `print_values` function is now a new object, but any bindings to the "old" version of the function remain.

# So, in general, stay away from reloading modules dynamically.
