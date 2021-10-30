#Implement a generator which will generate odd numbers endlessly

def endless_odd():
    n=-1
    while True:
        n+=2
        yield n

gen = endless_odd()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))