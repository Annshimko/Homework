# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:

# 1) characters that appear in all strings

# 2) characters that appear in at least one string

# 3) characters that appear at least in two strings

# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

import string


def test_2(string_list=None):  # list of characters at least once in strings
    string_list = string_list or []
    character_set = set()
    for string in string_list:
        character_set = character_set.union(set(string))
    return character_set


def character_frequency(string_list=None):
    string_list = string_list or []
    frequency_dictionary = {}
    character_list = test_2(string_list)
    for character in character_list:
        counter = 0
        for string in string_list:
            if character in string:
                counter += 1
        frequency_dictionary[character] = counter
    return frequency_dictionary


def test_1(string_list=None):
    string_list = string_list or []
    result_list = []
    for character in character_frequency(string_list):
        if character_frequency(string_list)[character] >= len(string_list):
            result_list.append(character)
    return result_list


def test_3(string_list=None):
    string_list = string_list or []
    result_list = []
    for character in character_frequency(string_list):
        if character_frequency(string_list)[character] >= 2:
            result_list.append(character)
    return result_list


def test_4(string_list=None):  # list of characters not in string
    string_list = string_list or []
    result_set = set()
    for character in string.ascii_letters:
        if character not in test_2(string_list):
            result_set.add(character)
    return result_set


test_strings = ['This', 'string', 'is', 'Awesome']
print('Letters, which appear at least once in strings: ')
print(test_2(test_strings))
# print('Frequency dictionary: ')
# print(character_frequency(test_strings))
print('Letters, which appear at least once in all strings: ')
print(test_1(test_strings))  # appears in all strings
print('Letters, which appear at least in 2 strings: ')
print(test_3(test_strings))  # appears at least in 2 strings
print("Letters, which doesn't appear: ")
print(test_4(test_strings))  # characters not in strings
