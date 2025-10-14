'''Logic:
The first item in the dictionary is the least recently used (LRU).
The last item in the dictionary is the most recently used (MRU).
Every get or put operation moves the key to the end.
If the cache is full, remove the first key before adding a new one.'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            v = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = v
            return v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                for k in self.cache.keys():
                    self.cache.pop(k)
                    break
            self.cache[key] = value
