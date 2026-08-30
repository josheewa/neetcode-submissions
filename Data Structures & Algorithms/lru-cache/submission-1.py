class LRUCache:

    def __init__(self, capacity: int):
        self.t = 0
        self.d = {}
        self.c = capacity
        self.times = {}
        

    def get(self, key: int) -> int:
        self.t += 1
        if key in self.d:
            self.times[key] = self.t
            return self.d[key]
        return -1 
        

    def put(self, key: int, value: int) -> None:
        self.t += 1
        if key in self.d:
            self.d[key] = value
        elif len(self.d) < self.c:
            self.d[key] = value
        else:
            heap = [(v, k) for k, v in self.times.items()]
            heapq.heapify(heap)
            lru = heapq.heappop(heap)[1]
            del self.d[lru]
            del self.times[lru]
            self.d[key] = value
        self.times[key] = self.t

