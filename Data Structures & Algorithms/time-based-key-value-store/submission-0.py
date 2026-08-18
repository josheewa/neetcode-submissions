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


        arr = self.tmap[key]
        p = 0
        q = len(arr) - 1

        while p <= q:
            m = (p + q) // 2
            if arr[m][1] == timestamp:
                return arr[m][0]
            if q - p <= 1:
                if arr[q][1] <= timestamp:
                    return arr[q][0]
                if arr[p][1] <= timestamp:
                    return arr[p][0]
                else:
                    return arr[p-1][0] if p-1 > -1 else ""

            if arr[m][1] < timestamp:
                p = m + 1
            else:
                q = m - 1

        return ""