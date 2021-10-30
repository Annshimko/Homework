#Task 7.8

#Implement your custom iterator class called MySquareIterator which gives squares of elements of collection
# it iterates through.

class EvenRange():

    def __init__(self, start_value, stop_value):
        self.start_value = start_value
        self.stop_value = stop_value
        self.n = start_value

    def __next__(self):
        if self.n <= self.stop_value-1 and self.n % 2 !=0:
            self.n += 1
        elif self.n <= self.stop_value - 2 and self.n % 2 == 0:
                self.n += 2
        else:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self

a = EvenRange(1, 10)
for i in a:
    print(i)