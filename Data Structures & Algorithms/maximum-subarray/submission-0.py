class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        subsum = 0
        
        for x in nums:
            if subsum < 0:
                subsum = x
            else:
                subsum += x
            res = max(res, subsum)
        return res

        

