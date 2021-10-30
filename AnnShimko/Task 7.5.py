#Task 7.5

#Implement function for check that number is even and is greater than 2.
# Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception
# (not Base Exception class).

class MyError(ValueError):
    def __init__(self, value):
        self.value = value
        if self.value % 2 != 0:
            self.message = 'Not even input error'
        elif self.value <= 2:
            self.message = 'Less than two input  error'
        else:
            self.message = None

    def __str__(self):
            return f'{self.message}'

def check(number):
    if MyError(number):
        print(MyError(number))

check(7)
