#Task 4.6
#Implement a function `get_shortest_word(s: str) -> str` which returns the
#longest word in the given string. The word can contain any symbols except
#whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
#the string with a same length return the word that occures first.
#Example:
#get_longest_word('Python is simple and effective!')
#'effective!'
#get_longest_word('Any pythonista like namespaces a lot.')
#'pythonista'

def get_longest_word(string):
  longest_word=''
  word_list = string.split()
  print(word_list)
  for word in word_list:
    if len(word) >len(longest_word):
      longest_word = word
  return longest_word

print(get_longest_word(input('Please, enter a phrase for analysis: ')))