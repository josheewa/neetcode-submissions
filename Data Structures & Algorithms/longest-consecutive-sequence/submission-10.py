class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(x):
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            
            parent[pb] = pa
        
        ns = set(nums)
        parent = {n:n for n in ns}
        for n in set(nums):
            if n-1 in parent:
                union(n, n-1)
            if n+1 in parent:
                union(n, n+1)

        grps = defaultdict(int)
        res = 0

        for x in parent:
            root = find(x)
            grps[root] += 1
            res = max(res, grps[root])
        
        return res
        