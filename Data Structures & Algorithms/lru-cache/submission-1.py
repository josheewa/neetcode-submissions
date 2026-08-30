class LRUCache:

    def __init__(self, capacity: int):
        self.lst = {}
        self.lru = None
        self.mru = None
        self.c = capacity

    def touch(self, key):
        if self.mru == key: return
        tmpprev = self.lst[key][1]
        tmpnext = self.lst[key][2]
        if self.lru == key:
            self.lru = tmpnext
        if tmpprev is not None:
            self.lst[tmpprev][2] = tmpnext
        if tmpnext is not None:
            self.lst[tmpnext][1] = tmpprev
        self.lst[key][1] = self.mru
        self.lst[key][2] = None
        self.lst[self.mru][2] = key
        self.mru = key

        

    def get(self, key: int) -> int:
        if key in self.lst:
            self.touch(key)
            return self.lst[key][0]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.lst:
            self.touch(key)
            self.lst[key][0] = value
        elif len(self.lst) < self.c:
            if self.lru is None: self.lru = key
            if self.mru is not None:
                self.lst[self.mru][2] = key
            self.lst[key] = [value, self.mru, None]
            self.mru = key
        else:
            tmplru = self.lru
            self.lru = self.lst[tmplru][2]
            if self.lru is None: print(tmplru, key)

            if self.lru is not None: self.lst[self.lru][1] = None
            del self.lst[tmplru]
            if self.mru == tmplru: self.mru = None

            if self.mru is not None: self.lst[self.mru][2] = key
            self.lst[key] = [value, self.mru, None]
            self.mru = key

        
