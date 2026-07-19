class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        starters = set()

        for n in nums:
            if n not in seen:
                if n-1 not in seen:
                    starters.add(n)
            seen.add(n)
        res = 0
        for s in starters:
            x = s
            c = 0
            while x in seen:
                x += 1
                c += 1
            res = max(res, c)

        return res