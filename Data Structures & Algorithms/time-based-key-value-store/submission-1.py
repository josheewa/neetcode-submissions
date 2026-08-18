class TimeMap:

    def __init__(self):
        self.tmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap:
            self.tmap[key].append((value, timestamp))
        else:
            self.tmap[key] = [(value, timestamp)]


    def get(self, key: str, timestamp: int) -> str:
        if not key in self.tmap: return ""

        res = ""
        arr = self.tmap.get(key, [])
        p = 0
        q = len(arr) - 1

        while p <= q:
            m = (p + q) // 2

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                p = m + 1
            else:
                q = m - 1

        return res