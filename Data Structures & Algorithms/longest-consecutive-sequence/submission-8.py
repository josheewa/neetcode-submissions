class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        starts = set()

        for n in ns:
            if n-1 not in ns: starts.add(n)
        
        res = 0
        for s in starts:
            x = s
            c = 0
            while x in ns:
                x += 1
                c += 1
            res = max(c, res)
        return res
