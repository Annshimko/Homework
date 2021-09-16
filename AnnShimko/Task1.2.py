# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

my_string = input('Please, enter a string to count character frequency: ')

my_string = my_string.casefold()
character_counter = {}
for character in set(my_string):
    character_counter[character] = my_string.count(character)

print(character_counter)
