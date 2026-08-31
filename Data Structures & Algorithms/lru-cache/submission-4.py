class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.c = capacity
    
    def touch(self, key: int):
        val = self.cache.pop(key)
        self.cache[key] = val
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.touch(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.touch(key)
        elif len(self.cache) == self.c:
            self.cache.popitem(last=False)
        self.cache[key] = value
        
