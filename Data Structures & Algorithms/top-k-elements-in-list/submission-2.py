class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        bucks = [[] for _ in range(len(nums)+1)]
        for n in freq:
            bucks[freq[n]].append(n)
            
        res = []
        for i in range(len(nums), 0, -1):
            res.extend(bucks[i])
            if len(res) == k:
                return res