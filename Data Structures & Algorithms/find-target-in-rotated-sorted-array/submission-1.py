class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = 0
        q = len(nums) - 1

        while q - p >= 0:
            m = (p + q) // 2
            for x in (p, m, q):
                if nums[x] == target: return x

            if nums[p] < nums[m] < nums[q]:
                if target < nums[m]: q = m - 1
                else: p = m + 1
            elif nums[p] < nums[m] > nums[q]:
                if nums[p] < target < nums[m]: q = m - 1
                else: p = m + 1
            elif nums[p] > nums[m] < nums[q]:
                if nums[m] < target < nums[q]: p = m + 1
                else: q = m - 1
            else: 
                return -1
        return -1