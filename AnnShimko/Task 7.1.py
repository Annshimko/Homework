#Task 7.1

#Implement class-based context manager for opening and working with file,
# including handling exceptions. Do not use 'with open()'.
# Pass filename and mode via constructor.

import io
from io import UnsupportedOperation


class UseFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.name, self.mode)
        except IOError:
            self.file = open(self.name, "w")
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.close()
            print(f'An error occured: {exc_val}')
            return exc_type
        self.file.close()



with UseFile('hello1.txt', 'r') as f:
    f.write('hello world!!!!')





