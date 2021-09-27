# Task 4.5
# Implement a decorator `remember_result` which remembers last result of function it decorates
# and prints it before next call.
#@remember_result
#def sum_list(*args):
#	result = ""
#	for item in args:
#		result += item
#	print(f"Current result = '{result}'")
#	return result
# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'"
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'"
# >>> "Current result = '12'"


def remember_result(func):
    def wrapper(*args, **kwargs):
        global last_result
        print('last result=', last_result)
        last_result = func(*args, **kwargs)
        return last_result
    return wrapper


@remember_result
def sum_list(*args):
    result = 0
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


last_result = None
sum_list(1, 2)
sum_list(2, 3)
sum_list(3, 4)