class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        curr = 1
        for i, n in enumerate(nums):
            output[i] = curr
            curr *= n

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= curr
            curr *= nums[i]
        
        return output
