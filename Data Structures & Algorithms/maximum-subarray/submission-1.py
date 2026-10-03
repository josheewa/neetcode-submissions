class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        curr = nums[0]

        for x in nums[1:]:
            curr = max(x, curr+x)
            res = max(res, curr)
        return res