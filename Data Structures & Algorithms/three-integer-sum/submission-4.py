class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1
        
        triples = set()

        for i in range(n):
            for j in range(i+1, n):
                x = nums[i]
                y = nums[j]
                freq[x] -= 1
                freq[y] -= 1

                if -x-y in freq and freq[-x-y] > 0:
                    triples.add(tuple(sorted([x, y, -x-y])))
                    
                freq[x] += 1
                freq[y] += 1

        res = []
        for x, y, z in triples:
            res.append([x, y, z])
        return res