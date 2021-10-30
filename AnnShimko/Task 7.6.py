#Task 7.6

#Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result.
# For pressing 'q' program succesfully close.
# Use function from Task 5.5 for validating input,
# handle all exceptions and print user friendly output.

class MyError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value % 2 != 0:
            self.message = 'Not even input error'
            return (self.message)
        if self.value <= 2:
            self.message = 'Less than two input  error'
            return (self.message)
def eratosthenes(n):
    primes = list (range(2, n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes

def odd_primes(N):
    oddprimes = eratosthenes(N)
    oddprimes.remove(2)
    return(oddprimes)

def goldbach(N):
    x, y = 0, 0
    result = 0
    if N % 2 == 0:
        prime = odd_primes(N)
        while result != N:
            for i in range(len(prime)):
                if result == N: break
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == N: break
    return x, y
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
        return MyError(number)


number = input('Please, enter a number:')
if number == 'q':
    exit()
else:
    try:
        N = int(number)
    except Exception as error:
        exit(f'number input error:{error}')
    if check(N) != 'None':
        print(goldbach(N))

