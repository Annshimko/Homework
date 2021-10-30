#Implement a generator which will geterate Fibonacci numbers endlessly.

def endless_fibonacci():
    a = 0
    b = 1
    while True:
        res = a + b
        a = b
        b = res
        yield res

gen = endless_fibonacci()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


