class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        else:
            arr = self.arr
            p = 0
            q = len(arr)
            while p < q:
                m = (p+q) // 2

                if arr[m] < num:
                    p = m+1
                else:
                    q = m
            self.arr.insert(p, num)

    def findMedian(self) -> float:
        m = (len(self.arr)-1) // 2
        if len(self.arr) % 2:
            return float(self.arr[m])
        return (self.arr[m] + self.arr[m+1]) / 2
