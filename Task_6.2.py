#### Task 4.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
# Example:
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
# ["bar"]

class HistoryDict():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.history = []

    def set_value(self, key, value):
        self.dictionary.update({key: value})
        if key not in self.history:
            self.history.append(key)
            if len(self.history) > 10:
                self.history.pop(0)

    def get_history(self):
        return self.history


d = HistoryDict({'Physics': 67, 'Maths': 87})
d.set_value('a', 2)
d.set_value('a', 2)
d.set_value('a', 2)
d.set_value('b', 2)
d.set_value('c', 2)
d.set_value('d', 2)
d.set_value('e', 2)
d.set_value('f', 2)
d.set_value('g', 2)
d.set_value('h', 2)
d.set_value('i', 2)
d.set_value('g', 2)
d.set_value('j', 2)
d.set_value('k', 2)
d.set_value('l', 2)
print(d.dictionary)
print(d.get_history())
