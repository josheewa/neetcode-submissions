class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = 0
        q = len(nums) - 1

        while p <= q:
            m = (p+q) // 2
            if nums[m] == target: return m
            if nums[m] < target: p = m + 1
            if nums[m] > target: q = m - 1
            
        return -1