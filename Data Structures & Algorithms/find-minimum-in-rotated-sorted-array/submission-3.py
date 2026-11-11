class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = 0
        q = len(nums)-1

        while p <= q:
            if nums[p] <= nums[q]:
                return nums[p]
            
            m = (p+q)//2
            if nums[p] <= nums[m]:
                p = m+1
            else:
                q = m