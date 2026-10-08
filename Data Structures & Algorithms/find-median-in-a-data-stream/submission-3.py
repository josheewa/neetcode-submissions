class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        else:
            arr = self.arr
            for i in range(len(arr)):
                if arr[i] == num or arr[i] > num:
                    self.arr.insert(i, num)
                    return

            self.arr.append(num)
        
                
        

    def findMedian(self) -> float:
        m = (len(self.arr)-1) // 2

        if len(self.arr) % 2:
            return float(self.arr[m])
        return (self.arr[m] + self.arr[m+1]) / 2
