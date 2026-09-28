class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        seen = [[False]*n for _ in range(m)]

        def dfs(i, j):
            seen[i][j] = True
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n:
                    if not seen[ni][nj] and grid[ni][nj] == "1":
                        dfs(ni, nj)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if seen[i][j] or grid[i][j] == "0": continue
                dfs(i, j)
                res += 1
        return res

