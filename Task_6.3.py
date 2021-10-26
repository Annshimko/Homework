# Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching
# to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used
# in alphabetical order, excluding those already used in the key.
#
# Keyword is "Crypto"
# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:

# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

class Crypto:

    def __init__(self, word):
        self.alphabet = [character for character in string.ascii_uppercase]
        self.word = word.upper()
        self.crypto_alphabet = []
        self.decoding_dictionary = {}

    def encode(self, phrase):
        for character in self.word:
            self.crypto_alphabet.append(character)
            self.alphabet.remove(character)
        self.crypto_alphabet += self.alphabet
        i = 0
        for character in string.ascii_uppercase:
            self.decoding_dictionary[character] = self.crypto_alphabet[i]
            i += 1

        encoded_phrase = ''
        for character in phrase:
            if character in string.ascii_letters:
                if character.isupper():
                    encoded_phrase += self.decoding_dictionary[character]
                else:
                    encoded_phrase += self.decoding_dictionary[character.upper()].lower()
            else:
                encoded_phrase += character
        return encoded_phrase


import string

c = Crypto('crypto')
print(c.encode("Hello, world"))
