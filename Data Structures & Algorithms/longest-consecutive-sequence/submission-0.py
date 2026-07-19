class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        
        res = 1
        prev = nums[0]
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                curr += 1
                res = max(res, curr)
            elif nums[i] == prev:
                continue
            else:
                curr = 1
            prev = nums[i]

        return res