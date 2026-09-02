class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        starts = set()

        for n in nums:
            if n-1 not in seen:
                starts.add(n)
        res = 0
        for s in starts:
            x = s
            curr = 0
            while x in seen:
                curr += 1
                x += 1
            res = max(curr, res)
        return res
        