class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def aux(i, temp):
            if i == len(nums):
                res.append(temp)
                return

            aux(i+1, temp)
            aux(i+1, temp + [nums[i]])
            
        aux(0, [])

        return res