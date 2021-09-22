# Task 4.11
# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values should be summarized in case of identical keys

# def combine_dicts(*args):
# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}
# print(combine_dicts(dict_1, dict_2)
# {'a': 300, 'b': 200, 'c': 300}
# (combine_dicts(dict_1, dict_2, dict_3)
# {'a': 600, 'b': 200, 'c': 300, 'd': 100}

def combine_dicts(*args):
    final_dictionary = {}
    for dictionary in args:
        for key, value in dictionary.items():
            if key in final_dictionary:
                final_dictionary[key] = final_dictionary[key] + value
            else:
                final_dictionary[key] = value

    return final_dictionary


print(combine_dicts({'a': 300, 'b': 200, 'c': 300},
                    {'a': 600, 'b': 200, 'c': 300, 'd': 100},
                    {'e': 100, 'r': 1000}))
