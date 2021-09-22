### Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.

def quotes_replacer(string):
  new_string=str()
  for character in string:
    if character == "'":
      new_string+='"'
    elif character == '"':
      new_string += "'"
    else:
      new_string += character
  return new_string

print(quotes_replacer(input('Please, enter a string:')))