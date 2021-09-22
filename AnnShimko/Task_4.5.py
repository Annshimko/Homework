# Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.
# Example:
#split_by_index(87178291199)
#(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

def get_digits(number):
  string_number = str(number)
  result_tuple = tuple(int(digit) for digit in string_number)
  return result_tuple

print(get_digits(123412345))