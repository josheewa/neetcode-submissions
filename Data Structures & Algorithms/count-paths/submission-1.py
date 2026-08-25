class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mp = {}
        def aux(i, j):
            if (i,j) in mp: return mp[i,j]
            if i == m-1 or j == n-1: return 1
            if i > m-1 or j > n-1: return 0

            res = aux(i+1, j) + aux(i, j+1)
            mp[i,j] = res
            return res
        return aux(0,0)