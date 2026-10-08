class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        else:
            arr = self.arr
            
            p = 0
            q = len(arr) - 1
            m = 0
            while p <= q and 0 <= p < len(arr) and 0 <= q < len(arr):
                if p == q:
                    if arr[p] == num or arr[p] > num:
                        self.arr.insert(p, num)
                    elif arr[p] < num:
                        self.arr.insert(p+1, num)
                    return
                m = (p+q) // 2

                if arr[m] == num:
                    self.arr.insert(m, num)
                    return
                if arr[m] < num:
                    p = m+1
                else:
                    q = m-1
            self.arr.insert(p, num)
                
        

    def findMedian(self) -> float:
        m = (len(self.arr)-1) // 2
        if len(self.arr) % 2:
            return float(self.arr[m])
        return (self.arr[m] + self.arr[m+1]) / 2
