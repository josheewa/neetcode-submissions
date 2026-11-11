class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = 0
        q = len(nums)-1

        while p < q:
            m = (p+q)//2
            if nums[p] <= nums[m] <= nums[q]:
                return nums[p]
            if nums[p] >= nums[m] <= nums[q]:
                q = m
            if nums[p] <= nums[m] >= nums[q]:
                p = m+1
        return nums[p]