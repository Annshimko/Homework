### Task 6.1
#Implement a Counter class which optionally accepts the start value and the counter stop value.
#If the start value is not specified the counter should begin with 0.
#If the stop value is not specified it should be counting up infinitely.
#If the counter reaches the stop value, print "Maximal value is reached."

#Implement two methods: "increment" and "get"

#* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

class Counter:
    #start = 0
    #stop = None

    def __init__(self, start = 0, stop = None):
        self.stop = stop
        self.value = start

    def __repr__(self):
        return (f'value= {self.value!r}')

    def increment(self):
        if self.stop:
            if self.value < self.stop:
                self.value += 1
                return self.value
            else:
                print('Maximal value is reached')
                return self.stop
        else:
            self.value += 1
            return self.value

    def get (self):
        print(self.value)
        return (f'value= {self.value!r}')





c = Counter()
c.increment()
c.get()
c.increment()
c.get()
b = Counter(7, 10)
b.increment()
b.get()
b.increment()
b.get()
b.increment()
b.get()
b.increment()
b.get()