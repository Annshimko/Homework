# Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form.
# Examples:
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']

word_list = input('Please, enter comma separated sequence of words: ').split(',')
unique_words = sorted(set(word_list))
print(unique_words)
