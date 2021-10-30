#Task 7.8

#Implement your custom iterator class called MySquareIterator which gives squares of elements of collection
# it iterates through.

class MySquareIterator():

    def __init__(self, value):
        self.value = value
        self.sqr_list = [i**2 for i in self.value]

    def __next__(self):
        if self.n < len(self.sqr_list):
            self.n += 1
            return self.sqr_list[self.n - 1]
        else:
            raise StopIteration

    def __iter__(self):
        self.n = 0
        return self

lst=[1,2,3,4]
itr = MySquareIterator(lst)
for i in itr:
    print(i)