#Task 7.4
#Implement decorator for supressing exceptions. If exception not occure write log to console.


def exception_wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                print(f'Result:{res}')

            except Exception as error:
                exit(f'An error occured: {error} ')

        return wrapper

@exception_wrapper
def calculation(a, b):
    return (2*a+a**3)/b

a, b = map(int, (input('Введите  a b')).split())
calculation(a,b)