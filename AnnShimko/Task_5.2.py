# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

# def most_common_words(filepath, number_of_words=3):
#    pass

# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']

import collections
import string


def most_common_words(filepath, number_of_words):
    lines = ''
    with open(filepath, 'r') as text:
        for line in text.readlines():
            for character in string.punctuation:
                line = line.replace(character, ' ')
            lines += line
    word_counter = collections.Counter(lines.split())
    return [word[0]for word in word_counter.most_common(number_of_words)]


filepath = 'data/lorem_ipsum.txt'

print(most_common_words(filepath, 3))
