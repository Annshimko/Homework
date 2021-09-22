### Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse)

def str_split(string, separator=None, maxsplit = None):
  str_list = []


  if separator is None:
    separator = ' '
    string = string.strip()
    i = 0
    while i < len(string) - 1:
      if string[i] == separator and string[i + 1] == separator:
        string = string[:i] + string[i + 2:]
      i += 1

  maxsplit = maxsplit or string.count(separator)
  for i in range (min(maxsplit, string.count(separator))):
    str_list.append(string[:string.index(separator)])
    string=string[string.index(separator)+1:]
  str_list.append(string)
  return str_list


test_string = '  Never,   ever, again      '
print(str_split(test_string,' ', 3), '\t','<- str_split')
print((test_string.split(' ', 3)), '\t' ,'<- split')
print()
print(str_split(test_string,maxsplit= 3), '\t','<- str_split')
print((test_string.split(maxsplit = 3)), '\t' ,'<- split')
print()
print(str_split(test_string,','), '\t','<- str_split')
print((test_string.split(',')), '\t' ,'<- split')
print()
print(str_split(test_string), '\t','<- str_split')
print((test_string.split()), '\t' ,'<- split')