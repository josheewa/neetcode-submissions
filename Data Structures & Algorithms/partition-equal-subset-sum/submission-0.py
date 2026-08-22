class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for x in nums: total += x
        if total % 2 != 0: return False

        target = total // 2

        # we only need to check if we can make target from elements in the set
        freq = defaultdict(int)
        for x in nums: freq[x] += 1
        lo = min(nums)

        def aux(t):
            if t < lo: return False
            if t == 0 or t in freq and freq[t] > 0: return True

            for x in freq:
                if freq[x] == 0: continue
                freq[x] -= 1
                if aux(t-x): return True
                freq[x] += 1
            return False

        return aux(target)