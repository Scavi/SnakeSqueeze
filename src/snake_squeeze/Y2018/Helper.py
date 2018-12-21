class Cache:
    def __init__(self):
        self.cache = dict()
        self.order = []


    def add(self, key, value):
        self.cache[key] = value
        self.order.append(value)


    def has(self, key):
        return key in self.cache


    def pos_of(self, lookup):
        for i in range(len(self.order)):
            if self.order[i] == lookup:
                return i
        return -1
