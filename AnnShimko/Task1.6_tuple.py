# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:

# Input: (1, 2, 3, 4)
# Output: 1234

given_tuple = (1, 2, 3, 4,)
line = ''
for number in given_tuple:
    line += str(number)
integer_result = int(line)
print(integer_result)
