# Task 5.1
#Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
# `sorted_names.txt`. Each name should start with a new line as in the following example:
#Adele
#Adrienne
#...
#Willodean
#Xavier

with open('data/unsorted_names.txt') as names:
    with open('data/sorted_names.txt','w') as file:
            file.writelines(sorted(list(names)))
