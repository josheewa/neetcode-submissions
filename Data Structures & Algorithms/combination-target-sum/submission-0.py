class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        
        def aux(idx, lst, tot):
            if tot == target:
                res.append(lst)
                return
            
            for i in range(idx, len(nums)):
                n = nums[i]
                if n + tot <= target:
                    aux(i, lst + [n], n + tot)
                else: break
        aux(0, [], 0)
        return res

