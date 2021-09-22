# Task 4.7
#Implement a function `foo(List[int]) -> List[int]` which, given a list of
#integers, return a new list such that each element at index `i` of the new list
#is the product of all the numbers in the original array except the one at `i`.
#Example:
#foo([1, 2, 3, 4, 5])
#[120, 60, 40, 30, 24]

def foo(multiplier_list):
    if all(multiplier_list):
        total_product = 1
        for multiplier in multiplier_list:
            total_product *= multiplier

        result = []
        for multiplier in multiplier_list:
            result.append(int(total_product / multiplier))
        return result
    else:
        return "Division by zero Error"

print(foo([1, 2, 3, 4, 5]))

print(foo(list(map(int, input('Please, enter data: ').split()))))