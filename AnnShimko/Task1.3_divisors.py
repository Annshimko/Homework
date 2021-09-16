# Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors]
# (https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

number = int(input('Enter a number, please: '))
divisor = 1
divisors_set=set()
while divisor not in divisors_set:
  if number % divisor == 0:
    divisors_set.add(divisor)
    divisors_set.add(number // divisor)
  divisor +=1
print(sorted(divisors_set))
