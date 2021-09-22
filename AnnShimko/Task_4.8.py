# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]

def get_pairs(my_list):
    if len(my_list) <= 1:
        return
    pairs = [tuple([my_list[i], my_list[i + 1]]) for i in range(len(my_list) - 1)]
    return pairs


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs([2]))
