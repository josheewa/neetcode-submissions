class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]): return
            if grid[r][c] == "0" or seen[r][c]: return
            seen[r][c] = True
            for i, j in dirs: dfs(r+i, c+j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or seen[i][j]: 
                    continue
                res += 1
                dfs(i, j)
        
        
        return res

