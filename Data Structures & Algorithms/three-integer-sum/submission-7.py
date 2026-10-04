class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            
            p, q = i+1, n-1
            while p < q and q < n:
                tsum = nums[i] + nums[p] + nums[q]
                if tsum == 0:
                    res.append([nums[i], nums[p], nums[q]])
                    p += 1
                    while p < q and nums[p-1] == nums[p]:
                        p += 1
                    q -= 1
                    while p < q and nums[q+1] == nums[q]:
                        q -= 1
                elif tsum < 0:
                    p += 1
                else:
                    q -= 1
        return res