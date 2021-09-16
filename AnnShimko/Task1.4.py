# Task 1.4
# Write a Python program to sort a dictionary by key.

dictionary = {'z': 1, 'b': 2, 'q': 3, 'n': 2, 'a': 2, 'l': 3}
sorted_dictionary = {}
for key in sorted(dictionary):
    sorted_dictionary[key] = dictionary[key]
print(sorted_dictionary)
