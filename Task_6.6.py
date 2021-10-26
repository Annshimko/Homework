# Task 4.6
# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.
# Example:
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# >>> True

class Sun:

    inst = None

    def __new__(self):
        if not Sun.inst:
            Sun.inst = object.__new__(Sun)
        return Sun.inst



a = Sun()
b = Sun()
c = Sun()
print(a is b)
print(a is c)