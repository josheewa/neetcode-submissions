class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        n = len(intervals)
        if n == 1: return intervals

        res = []
        p = intervals[0][0]
        q = intervals[0][1]
        for i in range(1, n):
            a, b = intervals[i]

            if p <= a <= q:
                q = max(q, b)
            else:
                res.append([p, q])
                p, q = a, b
        res.append([p,q])
        return res