class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        res = []
        for i in range(len(nums)):
            d[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            decs = []
            for j in range(i+1, len(nums)):
                d[nums[j]] -= 1
                decs.append(nums[j])
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                temp = -(nums[i] + nums[j])

                if d[temp] > 0:
                    res.append([nums[i], nums[j], temp])
            for x in decs:
                d[x] += 1

        return res
                