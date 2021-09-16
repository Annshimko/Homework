# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

my_string = input('Please, enter any string: ')

length = 0
for char in my_string:
    length += 1

print(length)
