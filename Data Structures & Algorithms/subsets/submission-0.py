class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def aux(i, temp):
            if i == len(nums):
                res.append(temp.copy())
                return

            aux(i+1, temp)
            temp.append(nums[i])
            aux(i+1, temp)
            temp.pop()
        aux(0, [])

        return res