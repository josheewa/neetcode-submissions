class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def aux(lst, used):
            if len(lst) == len(nums):
                res.append(lst)
                return

            for x in nums:
                if x in used: continue

                used.add(x)
                aux(lst + [x], used)
                used.remove(x)
        res = []
        aux([], set())
        return res