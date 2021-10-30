#Task 7.2
#Implement context manager for opening and working with file,
# including handling exceptions with @contextmanager decorator.

from contextlib import contextmanager

@contextmanager
def used_file(name):
    try:
        file = open(name, 'w')
        yield file
    except Exception as error:
        exit(f'An error occured: {error}')
    finally:
        file.close()

with used_file('hello.txt') as f:
    f.write('abcdefg')
    f.write('bb')