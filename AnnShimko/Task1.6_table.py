# Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:

# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28

y_min, y_max, x_min, x_max = map(int, input(
    'Please, enter 4 numbers (min and max values of multipliers): ').split())
print()
print('', end='\t')
for multiplier_x in range(x_min, x_max + 1):
    print(multiplier_x, end='\t')
print()
print()
for multiplier_y in range(y_min, y_max + 1):
    print(multiplier_y, end='\t')
    for multiplier_x in range(x_min, x_max + 1):
        print(multiplier_y * multiplier_x, end='\t')
    print()
