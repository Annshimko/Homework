# Task 4.4
# Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
# Implement str() function call for each class.


class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Bird {self.name}'

    def fly(self):
        return f'Bird {self.name} can fly'

    def walk(self):
        return f'Bird {self.name} can walk'


class FlyingBird(Bird):
    def __init__(self, name, ration=('flies', 'bugs')):
        super(FlyingBird, self).__init__(name)
        self.ration = ration

    def eat(self):
        return f'Bird {self.name} eats {self.ration}'


class NonFlyingBird:
    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration
        self.walk = Bird(self).walk

    def __str__(self):
        return f'{self.name}'

    def swim(self):
        return f'Bird {self.name} can swim'

    def eat(self):
        return f'Bird {self.name} eats {self.ration}'


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration=('fish', 'bugs')):
        super(SuperBird, self).__init__(name)
        self.ration = ration


duck = Bird('Duck')
print(duck.walk())
dove = FlyingBird('Dove', 'baton')
print(dove.walk())
print(dove.fly())
print(dove.eat())
pinguin = NonFlyingBird('Pinguin')
print(pinguin.walk())
print(pinguin.eat())
print(pinguin.swim())
# print(pinguin.fly())
seagull = SuperBird('seagull')
print(seagull.walk())
print(seagull.eat())
print(seagull.swim())
print(seagull.fly())
