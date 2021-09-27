### Task 4.7*
#Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
#Try to change x to a list `[1,2,3]`. Explain the result.
#Try to change import to `from x import *` where x - module names. Explain the result.

# The Solution:
# The command print(mod_c.x) retrieves the value of variable x from mod_c, where x=5

# After changing value of x to [1,2,3] and restarting mod_a there's no change in the result(x=5).
# To receive current value of x we need to import "reload" from importLib and call reload(mod_c).

# After changing import to `from x import *` the name of the module becomes unkown to our program, but now we can adress
# variables directly through their names (for example, we can call "print(x)" command). As we used *, all variables
# where loaded
# The reason is that we used "from" notation and loaded all variables and functions in module. Now we can adress functions
# directly using their names and don't need to call them through dot and module name.
