class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        reverse = defaultdict(list)
        for key in freq:
            reverse[freq[key]].append(key)

        topk = []
        x = len(nums)
        while len(topk) < k and x > 0:
            topk.extend(reverse[x])
            x -= 1
        return topk

            