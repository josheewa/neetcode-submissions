class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p = i+1
            q = len(nums)-1
            while p < q:
                pq = nums[p] + nums[q]
                if nums[i] + pq == 0:
                    res.append([nums[p], nums[q], nums[i]])
                    p += 1
                    q -= 1
                    while p < q and nums[p] == nums[p-1]:
                        p += 1
                    while p < q and nums[q] == nums[q+1]:
                        q -= 1
                elif nums[i] + pq > 0:
                    q -= 1
                else:
                    p += 1

        return res