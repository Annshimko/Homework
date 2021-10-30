#Task 7.3
#Implement decorator with context manager support for writing execution time to log-file.
# See contextlib module.
import time
from contextlib import contextmanager


def execution_time(func, name):
    @contextmanager
    def managed_file(name, *args, **kwargs):
        try:
            file = open(name, 'w')
            yield file
        except Exception as error:
            exit(f'An error occured: {error}')
        finally:
            file.close()
    t0= time.time()
    func()
    t1 = time.time()
    with managed_file(name) as  file:
        file.write(t1-t0)
    return managed_file

def x2(x):
    return(x**2)

execution_time(x2(23), 'log.txt')

