# Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.
# Examples:

# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_of_dictionaries = [
    {'name': 'Tim', 'age': 7, 'school': '#32'},
    {'name': 'Veronika', 'age': 4, 'school': '#62'},
    {'name': 'Tim', 'age': 5, 'school': '#144'},
]
set_of_unique_values = set()

for dictionary in list_of_dictionaries:
    for value in dictionary.values():
        set_of_unique_values.add(value)

print(set_of_unique_values)
