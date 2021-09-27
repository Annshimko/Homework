#Task 4.6
# Implement a decorator call_once which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.
#@call_once
#def sum_of_numbers(a, b):
#    return a + b

#print(sum_of_numbers(13, 42))
#>>> 55
#print(sum_of_numbers(999, 100))
#>>> 55
#print(sum_of_numbers(134, 412))
#>>> 55
#print(sum_of_numbers(856, 232))
#>>> 55

cache_dictionary = {}

def call_once(func):
    def wrapper(*args, **kwargs):
        global cache_dictionary
        if func in cache_dictionary:
            return cache_dictionary[func]
        else:
            cache_dictionary[func] = func(*args, **kwargs)
            return cache_dictionary[func]

    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

@call_once
def sum_of_numbers2(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))

print(sum_of_numbers2(134, 412))
print(sum_of_numbers2(856, 232))