#Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited.

def palindrome_test(string):
  string = string.lower()
  #according to wiki, we can ignore punctuation marks and spaces:
  for character in '''!()-[]{};?@#$%:'"\,./^&;*_''' :
    string = string.replace(character,'')
  for i in range(len(string)//2):
    if string[i] != string[-i-1]:
      return False
  return True

print(palindrome_test(input()))