# Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# split_by_index("no luck", [42])
# ["no luck"]

def split_by_index(string, list_of_indexes=None):
    list_of_indexes = list_of_indexes or []
    result_list = []
    start = 0
    for index in sorted(list_of_indexes):
        result_list.append(string[start: index])
        start = index
    if start < len(string):
        result_list.append(string[start:])
    return result_list


initial_string = "pythoniscool,isn'tit?"
index_list = [6, 8, 12, 13, 18]
print(split_by_index(initial_string, index_list))
print()
initial_string = input('Please, enter the string to split: ')
index_list = list(map(int, input('and the list of indexes:').split()))
print(split_by_index(initial_string, index_list))
